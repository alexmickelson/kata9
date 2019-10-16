import unittest
from models.checkoutrule import CheckoutRule
from models.prices import MultipleItemPrice


class TestCheckoutRule(unittest.TestCase):

    def test_can_get_sku_type(self):
        rule: CheckoutRule = CheckoutRule("A", 50, MultipleItemPrice(3, 130))
        self.assertEqual("A", rule.get_sku())

    def test_evalutate_price_on_quantity(self):
        rule: CheckoutRule = CheckoutRule("A", 50, MultipleItemPrice(3, 130))
        price: int = rule.evaluate_price(2)
        self.assertEqual(100, price)

    def test_evalutate_price_on_quantity_with_special_rule(self):
        rule: CheckoutRule = CheckoutRule("A", 50, MultipleItemPrice(3, 130))
        price: int = rule.evaluate_price(3)
        self.assertEqual(130, price)

    def test_evaluate_price_with_no_special_rule(self):
        rule: CheckoutRule = CheckoutRule("A", 50)
        actual: int = rule.evaluate_price(5)
        self.assertEqual(250, actual)
