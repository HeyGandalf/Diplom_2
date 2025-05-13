import allure
import requests

from helpers.endpoints import Urls, Handlers
from helpers.ingredients_data import Ingredient


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.description("Создание заказа авторизованным пользователем")
    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, create_user):
        token = create_user[3]
        headers = {'Authorization': token}
        response = requests.post(
            f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}",
            headers=headers,
            json=Ingredient.correct_ingredients
        )
        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"
        assert response.json().get("success") is True, f"Ожидалось success=True, но получено: {response.json()}"

    @allure.description("Создание заказа неавторизованным пользователем")
    @allure.title("Создание заказа неавторизованным пользователем")
    def test_create_order_not_auth(self):
        response = requests.post(
            f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}",
            json=Ingredient.correct_ingredients
        )
        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"
        assert response.json().get("success") is True, f"Ожидалось success=True, но получено: {response.json()}"

    @allure.description("Создание заказа без ингредиентов")
    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = requests.post(f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}")
        assert response.status_code == 400, f"Ожидался статус 400, но получен {response.status_code}"
        assert response.json()['message'] == "Ingredient ids must be provided", f"Сообщение не соответствует: {response.json()}"

    @allure.description("Создание заказа с невалидным хешем ингредиента")
    @allure.title("Создание заказа с невалидным хешем ингредиента")
    def test_create_order_invalid_hash_ingredient(self):
        response = requests.post(
            f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}",
            json=Ingredient.incorrect_ingredients
        )
        assert response.status_code == 500, f"Ожидался статус 500, но получен {response.status_code}"
        assert 'Internal Server Error' in response.text, f"Ответ не содержит 'Internal Server Error': {response.text}"