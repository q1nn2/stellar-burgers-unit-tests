from unittest.mock import Mock

import pytest

from stellar_burgers.bun import Bun
from stellar_burgers.burger import Burger
from stellar_burgers.ingredient import Ingredient
from tests.data import BUN_NAME, BUN_PRICE, INGREDIENT_DATA


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun_mock():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun


@pytest.fixture
def ingredient_mocks():
    ingredients = []
    for data in INGREDIENT_DATA:
        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = data["type"]
        ingredient.get_name.return_value = data["name"]
        ingredient.get_price.return_value = data["price"]
        ingredients.append(ingredient)
    return ingredients
