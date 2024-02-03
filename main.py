import logging

from fastapi import FastAPI, HTTPException, APIRouter

from src.core import http_util
from src.core.base_dto import ErrorResponseDTO

app = FastAPI(docs_url="/docs", openapi_url="/openapi", redoc_url=None)

# 로깅 레벨 설정 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.basicConfig(level=logging.INFO)

# Router Setting
master_router = APIRouter(
    responses={404: {"description": "Page Not Found"}},
)
http_util.router_setting(app, master_router)


# Server Health Check
@app.get("/health-check")
async def health_check():
    return "health check success"


# Error 처리
@app.exception_handler(HTTPException)
async def http_exception_handler(request, error_object):
    logging.error(f"시스템 오류가 발생했습니다. Error status_code: {error_object.status_code}, Message : {error_object.detail}")
    return ErrorResponseDTO.of(error_object)


@app.exception_handler(Exception)
async def http_exception_handler(request, error_object):
    logging.error(f"예상하지 못한 오류가 발생했습니다. Error: {error_object}")
    error_object = HTTPException(status_code=500, detail="예상하지 못한 오류가 발생했습니다. 관리자에게 문의하세요.")
    return ErrorResponseDTO.of(error_object)

