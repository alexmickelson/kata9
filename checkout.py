from typing import List, DefaultDict
from collections import defaultdict
from models.checkoutrule import CheckoutRule


class Checkout():

    def __init__(self, rules: List[CheckoutRule]):
        self.rules: List[CheckoutRule] = rules
        self.items: DefaultDict[str, int] = defaultdict(int)
        pass

    def get_total_cost(self) -> int:
        total_cost: int = 0
        for rule in self.rules:
            total_cost += rule.evaluate_price(self.items[rule.get_sku()])
        return total_cost

    def scan_items(self, goods: List[str]) -> None:
        for item in goods:
            self.items[item] += 1
