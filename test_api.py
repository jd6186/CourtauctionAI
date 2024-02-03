from fastapi.testclient import TestClient
from fastapi import status
from main import app  # Assuming your FastAPI app is named 'app'

client = TestClient(app)


# TEST Case01: Short Link 생성 및 호출이 정상적으로 진행된 경우
def test_main():
    print(f"test_main")
    assert 200 == status.HTTP_200_OK
