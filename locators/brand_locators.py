from selenium.webdriver.common.by import By

from core.locators import Locators


class BrandLocators(Locators):
    BRANDS_ELEMENTS = (By.CSS_SELECTOR, ".col-sm-3 a")
