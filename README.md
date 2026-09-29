# Stellar Burgers — Unit Tests

Юнит-тесты бизнес-логики класса `Burger` приложения Stellar Burgers.

## Что проверяется

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
- GitHub Actions

## Структура

```text
stellar-burgers-unit-tests/
├── stellar_burgers/
│   ├── bun.py
│   ├── burger.py
│   ├── database.py
│   ├── ingredient.py
│   └── ingredient_types.py
├── tests/
│   ├── conftest.py
│   ├── data.py
│   └── test_burger.py
├── htmlcov/
├── .github/workflows/
├── pytest.ini
├── requirements.txt
└── README.md
```

## Установка

```bash
git clone https://github.com/q1nn2/stellar-burgers-unit-tests.git
cd stellar-burgers-unit-tests
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

## Запуск

```bash
pytest
```

Проверка покрытия настроена в `pytest.ini`. Тестовый запуск завершается ошибкой, если покрытие `stellar_burgers.burger` ниже 100%.

HTML-отчёт покрытия сохраняется в `htmlcov/`. На Windows его можно открыть командой:

```powershell
start htmlcov\index.html
```
