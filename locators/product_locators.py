from selenium.webdriver.common.by import By

from core import Locators


class ProductLocators(Locators):
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[2]/li[1]/h2')
