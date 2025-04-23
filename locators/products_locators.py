from selenium.webdriver.common.by import By

from core.locators import Locators


class ProductsLocators(Locators):
    OPTION_SHOW = (By.ID, "input-limit")
    OPTION_SORT = (By.ID, "input-sort")
    PRODUCTS = (By.CLASS_NAME, "product-layout")
    PRODUCTS_NAMES = (By.TAG_NAME, "h4")
    PRODUCTS_PRICE = (By.CLASS_NAME, "price-new")
    PAGINATION = (By.CSS_SELECTOR, "div.col-sm-6.text-right")

    @staticmethod
    def x_path_product(product: str, method_price: str) -> tuple:
        """
        Returns the XPATH locator for the price by price type (New, Old, Tax).

        :param product: product name (part contained in the title).
        :param method_price: price type ('New', 'Old', 'Tax').
        :return : a border with the method by.xpath and formed by.
        :raises ValueError: If the price method is not supported.
        """
        match method_price:
            case "new":
                method = "price-new"
            case "old":
                method = "price-old"
            case "tax":
                method = "price-tax"
            case _:
                raise ValueError(f"Unsupported price method: {method_price}")

        xpath = (
            f"//div[@class='caption' and .//a[contains(text(), \"{product}\")]]"
            f"//span[@class='{method}']"
        )

        return By.XPATH, xpath
