# API Tests for Stellar Burgers

Автоматизированные тесты для проверки API сервиса Stellar Burgers. Покрываются сценарии создания, авторизации и удаления пользователя, а также создания и получения заказов.

## 🚀 Установка

1. Клонируй репозиторий:

```bash
git clone https://github.com/yourusername/stellar-burgers-api-tests.git
cd stellar-burgers-api-tests
```

2. Создай и активируй виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate   # для Mac/Linux
venv\Scripts\activate.bat  # для Windows
```

3. Установи зависимости:

```bash
pip install -r requirements.txt
```

## 🧪 Запуск тестов

Для запуска всех тестов:

```bash
pytest -v --alluredir=allure-results
```

## 📊 Генерация Allure отчёта

1. Убедись, что установлен [Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline).

2. Сгенерируй и открой отчёт:

```bash
allure serve allure-results
```

Или сохрани HTML:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## 🛠 Используемые технологии

- Python 3.9+
- Pytest
- Allure-pytest
- Requests
- Faker
