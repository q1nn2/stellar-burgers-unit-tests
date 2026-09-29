from unittest.mock import patch

import pytest

from tests.data import (
    EXPECTED_RECEIPT,
    EXPECTED_TOTAL_PRICE,
    MOVE_CASE_IDS,
    MOVE_CASES,
    REMOVE_CASE_IDS,
    REMOVE_CASES,
)


class TestBurger:
    def test_burger_initial_bun_is_none(self, burger):
        assert burger.bun is None

    def test_burger_initial_ingredients_are_empty(self, burger):
        assert burger.ingredients == []

    def test_set_buns_sets_selected_bun(self, burger, bun_mock):
        burger.set_buns(bun_mock)

        assert burger.bun is bun_mock

    def test_add_ingredient_adds_ingredient_to_end(self, burger, ingredient_mocks):
        first_ingredient, second_ingredient = ingredient_mocks

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)

        assert burger.ingredients == [first_ingredient, second_ingredient]

    @pytest.mark.parametrize(
        "index, expected_ingredients",
        REMOVE_CASES,
        ids=REMOVE_CASE_IDS,
    )
    def test_remove_ingredient_removes_item_by_index(
        self, burger, index, expected_ingredients
    ):
        burger.ingredients = ["first", "second", "third"]

        burger.remove_ingredient(index)

        assert burger.ingredients == expected_ingredients

    @pytest.mark.parametrize(
        "index, new_index, expected_ingredients",
        MOVE_CASES,
        ids=MOVE_CASE_IDS,
    )
    def test_move_ingredient_changes_item_position(
        self, burger, index, new_index, expected_ingredients
    ):
        burger.ingredients = ["first", "second", "third"]

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == expected_ingredients

    def test_get_price_calculates_total_price(
        self, burger, bun_mock, ingredient_mocks
    ):
        burger.set_buns(bun_mock)
        for ingredient in ingredient_mocks:
            burger.add_ingredient(ingredient)

        result = burger.get_price()

        assert result == EXPECTED_TOTAL_PRICE

    def test_get_receipt_builds_expected_receipt(
        self, burger, bun_mock, ingredient_mocks
    ):
        burger.set_buns(bun_mock)
        for ingredient in ingredient_mocks:
            burger.add_ingredient(ingredient)

        with patch.object(
            burger, "get_price", return_value=EXPECTED_TOTAL_PRICE
        ):
            result = burger.get_receipt()

        assert result == EXPECTED_RECEIPT
