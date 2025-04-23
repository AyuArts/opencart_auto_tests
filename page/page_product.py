from abc import ABC
from core.page import BasePage
from locators import ProductLocators as PL  # PL - products locators


class PageProduct(BasePage, ABC):
    def check_price_product(self, price: str) -> bool:
        return self._check_float(PL.PRODUCT_PRICE, price)
