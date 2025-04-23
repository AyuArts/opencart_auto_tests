import re
from abc import ABC
from config import settings
from core.page import BasePage
from utils.decorators import validate_option
from locators import ProductsLocators as PL  # PL - products locators


class PageProducts(BasePage, ABC):
    @validate_option(settings.default.options_filter_in_show)
    def check_filter_in_show(self, option_sort: str) -> bool:
        return self._check_dropdown_select(PL.OPTION_SHOW, option_sort)

    @validate_option(settings.default.options_filter_in_sort_by)
    def check_filter_in_sort_by(self, option_sort: str) -> bool:
        return self._check_dropdown_select(PL.OPTION_SORT, option_sort)

    @validate_option(settings.default.options_filter_in_show)
    def switch_filter_show(self, option_sort: str) -> None:
        self._select(PL.OPTION_SHOW, option_sort)

    @validate_option(settings.default.options_filter_in_sort_by)
    def switch_filter_in_sort_by(self, option_sort: str) -> None:
        self._select(PL.OPTION_SORT, option_sort)

    def check_count_products(self, count_products) -> bool:
        return self._check_count(PL.PRODUCTS, count_products)

    def check_text_pagination(self, pagination_text) -> bool:
        return self._check_text(PL.PAGINATION, pagination_text)

    def check_pagination_down_page(self):
        return self._check_element_is_displayed(PL.PAGINATION)

    def check_alphabet_order(self) -> bool:
        products = [el.text.lower() for el in self._find_elements(PL.PRODUCTS_NAMES)]
        return self._check_is_sorted_ascending(products)

    def check_price_order(self) -> bool:
        products_price = []

        for el in self._find_elements(PL.PRODUCTS_PRICE):
            text = el.text.strip()
            match = re.search(settings.reg.float, text)
            if match:
                price = float(match.group())
                products_price.append(price)
            else:
                self.log.warning(f"Failed to extract the price from: {text}")

        return self._check_is_sorted_ascending(products_price)

    def check_price_current_product(
        self, name_product: str, method_price: str, price: str
    ) -> bool:
        return self._check_float(PL.x_path_product(name_product, method_price), price)
