BUN_NAME = "Краторная булка N-200i"
BUN_PRICE = 1255.0

INGREDIENT_DATA = (
    {"type": "SAUCE", "name": "Соус Spicy-X", "price": 90.0},
    {"type": "FILLING", "name": "Мясо бессмертных моллюсков Protostomia", "price": 300.0},
)

REMOVE_CASES = (
    (0, ["second", "third"]),
    (1, ["first", "third"]),
    (2, ["first", "second"]),
)
REMOVE_CASE_IDS = ("remove_first", "remove_middle", "remove_last")

MOVE_CASES = (
    (0, 2, ["second", "third", "first"]),
    (2, 0, ["third", "first", "second"]),
    (1, 2, ["first", "third", "second"]),
)
MOVE_CASE_IDS = ("first_to_last", "last_to_first", "middle_to_last")

EXPECTED_TOTAL_PRICE = 2900.0
EXPECTED_RECEIPT = (
    "(==== Краторная булка N-200i ====)\n"
    "= sauce Соус Spicy-X =\n"
    "= filling Мясо бессмертных моллюсков Protostomia =\n"
    "(==== Краторная булка N-200i ====)\n\n"
    "Price: 2900.0"
)
