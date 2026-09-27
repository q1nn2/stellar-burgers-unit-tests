# Stellar Burgers — Unit Tests

Набор юнит-тестов для бизнес-логики класса `Burger` приложения Stellar Burgers.

## Возможности

Проверяется вся функциональность класса `Burger`:

- начальное состояние объекта;
- установка булочки;
- добавление ингредиентов;
- удаление ингредиента;
- перемещение ингредиента;
- расчёт итоговой стоимости;
- формирование чека.

Зависимости `Bun` и `Ingredient` изолированы с помощью моков. Для сценариев удаления и перемещения ингредиентов используется параметризация.

Покрытие класса `Burger` — **100%**.

## Стек

- Python
- pytest
- pytest-cov
- unittest.mock

## Структура

```text
stellar-burgers-unit-tests/
├── stellar_burgers/
│   ├── __init__.py
│   ├── bun.py
│   ├── burger.py
│   ├── database.py
│   ├── ingredient.py
│   └── ingredient_types.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── data.py
│   └── test_burger.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Установка

```bash
git clone https://github.com/q1nn2/stellar-burgers-unit-tests.git
cd stellar-burgers-unit-tests
git checkout develop1
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск

```bash
pytest
```

Проверка покрытия настроена в `pytest.ini`. Тестовый запуск завершается ошибкой, если покрытие `stellar_burgers.burger` ниже 100%.

Явный запуск с отчётом покрытия:

```bash
pytest --cov=stellar_burgers.burger --cov-report=term-missing
```
