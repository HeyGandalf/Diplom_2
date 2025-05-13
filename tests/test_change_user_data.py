import allure
import requests

from helpers.endpoints import Urls, Handlers
from helpers.user_data import User


@allure.suite('Изменение данных пользователя')
class TestChangeUserData:

    @allure.description("При попытке сменить email у авторизованного пользователя, изменение данных происходит успешно")
    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_change_user_email_with_auth(self, create_user):
        payload = {'email': User.create_user_data()["email"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['email'] == payload["email"]

    @allure.description("При попытке сменить password у авторизованного пользователя, изменение данных происходит успешно")
    @allure.title("Успешное изменение password авторизованного пользователя")
    def test_change_user_password_with_auth(self, create_user):
        payload = {'password': User.create_user_data()["password"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("При попытке сменить name у авторизованного пользователя, изменение данных происходит успешно")
    @allure.title("Успешное изменение name авторизованного пользователя")
    def test_change_user_name_with_auth(self, create_user):
        payload = {'name': User.create_user_data()["name"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200 and r.json()['user']['name'] == payload["name"]

    @allure.description("При попытке сменить данные пользователя без авторизации, возвращается ошибка")
    @allure.title("Изменение данных пользователя без авторизацией")
    def test_change_user_data_no_auth(self):
        r = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", data=User.create_user_data())
        assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'