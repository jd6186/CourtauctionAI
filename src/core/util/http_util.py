from fastapi import APIRouter, Depends

from src.api.guest import controller as guest_controller
from src.api.manager import controller as manager_controller
from src.api.user import controller as user_controller
from src.api.announcement import controller as announcement_controller
from src.api.authority import controller as authority_controller
from src.api.approval import controller as approval_controller
from src.api.terms import controller as terms_controller
from src.api.menu import controller as menu_controller
from src.api.product import controller as product_controller
from src.api.order import controller as order_controller
from src.api.notice import controller as notice_controller
from src.api.cooperation import controller as cooperation_controller
from src.api.settlement import controller as settlement_controller
from src.core.security import jwt_token_config


def cors_setting(app, CORSMiddleware):
    origins = [
        "*"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def url_routing_check(request):
    request_url = str(request.url)
    if '/health-check' in request_url:
        return
    if 'api' not in request_url:
        return
    print("############# request_url : ", request_url)


def router_setting(app, master_router):
    # master router에 연결할 router들 > db table 순서대로 정렬한 것 수정 금지
    announcement_router = APIRouter(prefix='/announcement', dependencies=[Depends(jwt_token_config.verify_token)])
    approval_router = APIRouter(prefix='/approval', dependencies=[Depends(jwt_token_config.verify_token)])
    authority_router = APIRouter(prefix='/authority', dependencies=[Depends(jwt_token_config.verify_token)])
    cooperation_router = APIRouter(prefix='/cooperation', dependencies=[Depends(jwt_token_config.verify_token)])
    guest_router = APIRouter(prefix='/guest')
    manager_router = APIRouter(prefix='/manager', dependencies=[Depends(jwt_token_config.verify_token)])
    menu_router = APIRouter(prefix='/menu', dependencies=[Depends(jwt_token_config.verify_token)])
    notice_router = APIRouter(prefix='/notice', dependencies=[Depends(jwt_token_config.verify_token)])
    order_router = APIRouter(prefix='/order', dependencies=[Depends(jwt_token_config.verify_token)])
    product_router = APIRouter(prefix='/product', dependencies=[Depends(jwt_token_config.verify_token)])
    settlement_router = APIRouter(prefix='/settlement', dependencies=[Depends(jwt_token_config.verify_token)])
    terms_router = APIRouter(prefix='/terms', dependencies=[Depends(jwt_token_config.verify_token)])
    user_router = APIRouter(prefix='/user', dependencies=[Depends(jwt_token_config.verify_token)])
    # banner_router = APIRouter(prefix='/banner', dependencies=[Depends(jwt_token_config.verify_token)])
    # cart_router = APIRouter(prefix='/cart', dependencies=[Depends(jwt_token_config.verify_token)])
    # certification_router = APIRouter(prefix='/certification', dependencies=[Depends(jwt_token_config.verify_token)])
    # department_router = APIRouter(prefix='/department', dependencies=[Depends(jwt_token_config.verify_token)])
    # event_router = APIRouter(prefix='/event', dependencies=[Depends(jwt_token_config.verify_token)])
    # file_router = APIRouter(prefix='/file', dependencies=[Depends(jwt_token_config.verify_token)])
    # manager_router = APIRouter(prefix='/manager', dependencies=[Depends(jwt_token_config.verify_token)])
    # margin_router = APIRouter(prefix='/margin???????????????', dependencies=[Depends(jwt_token_config.verify_token)])
    # payment_router = APIRouter(prefix='/payment', dependencies=[Depends(jwt_token_config.verify_token)])
    # popup_router = APIRouter(prefix='/popup', dependencies=[Depends(jwt_token_config.verify_token)])
    # promotion_router = APIRouter(prefix='/promotion', dependencies=[Depends(jwt_token_config.verify_token)])

    announcement_router.include_router(announcement_controller.router)
    approval_router.include_router(approval_controller.router)
    authority_router.include_router(authority_controller.router)
    cooperation_router.include_router(cooperation_controller.router)
    guest_router.include_router(guest_controller.router)
    manager_router.include_router(manager_controller.router)
    menu_router.include_router(menu_controller.router)
    notice_router.include_router(notice_controller.router)
    order_router.include_router(order_controller.router)
    product_router.include_router(product_controller.router)
    settlement_router.include_router(settlement_controller.router)
    terms_router.include_router(terms_controller.router)
    user_router.include_router(user_controller.router)

    master_router.include_router(announcement_router)
    master_router.include_router(approval_router)
    master_router.include_router(authority_router)
    master_router.include_router(cooperation_router)
    master_router.include_router(guest_router)
    master_router.include_router(manager_router)
    master_router.include_router(menu_router)
    master_router.include_router(notice_router)
    master_router.include_router(order_router)
    master_router.include_router(product_router)
    master_router.include_router(settlement_router)
    master_router.include_router(terms_router)
    master_router.include_router(user_router)

    app.include_router(master_router)

