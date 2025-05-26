import allure
import requests

from helpers.endpoints import Urls, Handlers
from helpers.ingredients_data import Ingredient


@allure.suite("Получение доступных заказов по пользователю")
class TestGetOrderUser:

    @allure.description("Получение доступных заказов авторизованного пользователя")
    @allure.title("Получение доступных заказов авторизованного пользователя")
    def test_get_user_orders_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        requests_create_order = requests.post(f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}", headers=token, data=Ingredient.correct_ingredients)
        response_get_order = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}", headers=token)
        assert response_get_order.status_code == 200 and response_get_order.json()['orders'][0]['number'] == requests_create_order.json()['order']['number']

    @allure.description("Получение заказов пользователя, если пользователь не авторизовался")
    @allure.title("Получение заказов без авторизации")
    def test_get_user_orders_no_auth(self):
        r = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}")
        assert r.status_code == 401 and r.json()['message'] == "You should be authorised"