import pytest
import requests
from helpers.endpoints import Urls, Handlers
from faker import Faker

fake = Faker()

@pytest.fixture(scope="function")
def create_user():
    # Генерация уникальных данных
    email = fake.email()
    password = fake.password()
    name = fake.first_name()

    # Удаление пользователя, если он уже существует
    existing_user_response = requests.post(f"{Urls.MAIN_URL}{Handlers.LOGIN_USER}", data={"email": email, "password": password})
    if existing_user_response.status_code == 200:  # Пользователь существует
        delete_response = requests.delete(f"{Urls.MAIN_URL}{Handlers.DELETE_USER}", headers={'Authorization': f"Bearer {existing_user_response.json()['token']}"})
        assert delete_response.status_code == 200, "Не удалось удалить существующего пользователя"

    # Создание нового пользователя
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", json=payload)

    assert response.status_code == 200, "Пользователь не создан"
    return email, password, name, response.json()['accessToken']
