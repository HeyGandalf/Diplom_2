import pytest
import requests
from helpers.endpoints import Urls, Handlers
from faker import Faker
import time

fake = Faker()

@pytest.fixture(scope="function")
def create_user():
    unique_email = f"{fake.email().split('@')[0]}_{int(time.time()*1000)}@{fake.email().split('@')[1]}"
    password = fake.password()
    name = fake.first_name()

    payload = {"email": unique_email, "password": password, "name": name}
    response = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", json=payload)

    if response.status_code == 403:
        raise Exception(f"User creation forbidden, possible duplicate email: {unique_email}")

    assert response.status_code == 200, "Пользователь не создан"
    access_token = response.json()['accessToken']

    yield unique_email, password, name, access_token

    headers = {'Authorization': access_token}
    delete_response = requests.delete(f"{Urls.MAIN_URL}{Handlers.DELETE_USER}", headers=headers)
    assert delete_response.status_code in [200, 202], "Не удалось удалить пользователя после теста"
