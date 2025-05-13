import allure
import requests

from helpers.endpoints import Urls, Handlers
from helpers.user_data import User


@allure.suite('Авторизация пользователя')
class TestLogin:

    @allure.description('При авторизации под пользователем, который есть в системе, происходит успешная авторизация')
    @allure.title('Авторизация под пользователем, который есть в системе')
    def test_login_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN_USER}', data=User.correct_data)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.description('При авторизации под пользователем с некорректным логином/паролем, срабатывает alert')
    @allure.title('Авторизация с некорректным логином/паролем')
    def test_login_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN_USER}', data=User.incorrect_data)
        assert response.status_code == 401 and response.json().get('success') == False