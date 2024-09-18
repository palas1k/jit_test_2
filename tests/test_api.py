import aiohttp
import pytest
from fastapi.testclient import TestClient
from main import app
from services import requester


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.mark.asyncio
async def test_get_user(client):
    """
    Тест для проверки получения информации о пользователе.
    """
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Leanne Graham",
        "email": "Sincere@april.biz"
    }


@pytest.mark.asyncio
async def test_get_user_not_found(client):
    """
    Тест для проверки получения информации о пользователе, которого нет в базе данных.
    """
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
