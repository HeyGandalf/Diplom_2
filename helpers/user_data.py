from faker import Faker

class User:

    @staticmethod
    def create_user_data():
        fake = Faker()
        return {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }

    correct_data = {
        "email": "jane_doe1751@yandex.ru",
        "password": "123qwe"
    }

    incorrect_data = {
        "email": "jane_doe175117@yandex.ru",
        "password": "123qwe"
    }

    double = {
        "email": "jane_doe1751@yandex.ru",
        "password": "123qwe",
        "name": "Jane"
    }

    without_email = {
        "email": "",
        "password": "123qwe",
        "name": "Jane"
    }

    without_password = {
        "email": "jane_doe1751@yandex.ru",
        "password": "",
        "name": "Jane"
    }

    without_name = {
        "email": "jane_doe1751@yandex.ru",
        "password": "123qwe",
        "name": ""
    }
