from selenium import webdriver
from config import settings


def get_driver():
    if settings.default.driver == "chrome":
        return webdriver.Chrome()
    elif settings.default.driver == "firefox":
        return webdriver.Firefox()
    elif settings.default.driver == "safari":
        return webdriver.Safari()


driver = get_driver()
