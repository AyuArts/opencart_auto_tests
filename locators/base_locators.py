from selenium.webdriver.common.by import By

from core.locators import Locators


class BaseLocators(Locators):
    MY_ACCOUNT_LINK = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')
    BRANDS_LINK = (By.XPATH, "//footer//a[text()='Brands']")
    DESKTOPS_LINK = (By.LINK_TEXT, "Desktops")
    SHOW_ALL_LINK = (By.LINK_TEXT, "Show All Desktops")
    CAMERAS_LINK = (By.LINK_TEXT, "Cameras")
    IPHONE_LINK = (By.LINK_TEXT, "iPhone")
    CURRENCY = (By.TAG_NAME, "strong")
    CURRENCY_DD = (By.CLASS_NAME, "fa-caret-down")
    CURRENCY_EURO = (By.NAME, "EUR")
    CURRENCY_POUND = (By.NAME, "GBP")
