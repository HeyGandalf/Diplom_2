import allure
import pytest
import requests
from helpers.endpoints import Urls, Handlers
from helpers.user_data import User

@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.description('Создание нового пользователя')
    @allure.title('Создание нового пользователя')
    def test_create_new_user_success(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', json=User.create_user_data())
        assert response.status_code == 200, f"Ожидался статус 200, но получен  {response.status_code}"
        assert response.json().get("success") is True, f"Ожидалось success=True, но получено: {response.json()}"

    @allure.description('При создании дублирующего пользователя возвращается ошибка')
    @allure.title('Создание пользователя который уже есть в системе')
    def test_create_double_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', json=User.double)
        assert response.status_code == 403, f"Ожидался статус 403, но получен  {response.status_code}"
        assert 'User already exists' in response.text, f"Ожидалось 'User already exists', но получено {response.text}"

    @allure.description('При создании пользователя с некорректными данными возвращается ошибка')
    @allure.title('Создание пользователя с некорректными данными')
    @pytest.mark.parametrize("user_data, expected_status, expected_message", [
        (User.without_email, 403, 'Email, password and name are required fields'),
        (User.without_password, 403, 'Email, password and name are required fields'),
        (User.without_name, 403, 'Email, password and name are required fields')
    ])
    def test_create_user_incorrect_data(self, user_data, expected_status, expected_message):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', json=user_data)
        assert response.status_code == expected_status, f"Ожидался статус {expected_status} , но получен {response.status_code}"
        assert expected_message in response.text, f"Ожидалось '{expected_message}' но получено {response.text}"
