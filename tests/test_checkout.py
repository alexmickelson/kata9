import unittest
from typing import List
from models.checkoutrule import CheckoutRule
from models.prices import MultipleItemPrice
from parameterized import parameterized
from checkout import Checkout


class TestCheckoutRule(unittest.TestCase):

    def setUp(self):
        rules: List[CheckoutRule] = []
        rules.append(CheckoutRule("A", 50, MultipleItemPrice(3, 130)))
        rules.append(CheckoutRule("B", 30, MultipleItemPrice(2, 45)))
        rules.append(CheckoutRule("C", 20))
        rules.append(CheckoutRule("D", 15))
        self.rules: List[CheckoutRule] = rules

    @parameterized.expand([
        (50, "A"),
        (100, "AA"),
        (130, "AAA"),
        (160, "ABAA"),
        (20, "C"),
        (100, "ABC"),
        (190, "DABABA")
    ])
    def test_totals(self, expected_cost: int, goods: str):
        checkout: Checkout = Checkout(self.rules)
        checkout.scan_items(goods)
        actual_cost: int = checkout.get_total_cost()
        self.assertEqual(expected_cost, actual_cost)
