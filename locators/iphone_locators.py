from selenium.webdriver.common.by import By

from core.locators import Locators


class IphoneLocators(Locators):
    BRANDS_LINK = (By.XPATH, "//footer//a[text()='Brands']")
    BRANDS_ELEMENTS = (By.CSS_SELECTOR, ".col-sm-3 a")
