from typing import Tuple
from models.prices import MultipleItemPrice


class CheckoutRule:

    def __init__(
            self,
            sku: str,
            singleItemPrice: int,
            multipleItemsPrice: MultipleItemPrice = MultipleItemPrice(-1, -1)):
        self.sku: str = sku
        self.itemPrice: int = singleItemPrice
        self.specialPrice: MultipleItemPrice = multipleItemsPrice

    def get_sku(self) -> str:
        return self.sku

    def handle_special_deals(self, quantity: int) -> Tuple[int, int]:
        price: int = 0
        if ((quantity // self.specialPrice.quantity) > 0):
            numSpecialApplies: int = quantity // self.specialPrice.quantity
            newQuantity: int = quantity % self.specialPrice.quantity
            price: int = numSpecialApplies * self.specialPrice.price
            return newQuantity, price
        else:
            return quantity, 0

    def handle_standard_pricing(self, quantity: int) -> int:
        return self.itemPrice * quantity

    def evaluate_price(self, quantity: int) -> int:
        price: int = 0
        quantity, price = self.handle_special_deals(quantity)
        price += self.handle_standard_pricing(quantity)
        return price
