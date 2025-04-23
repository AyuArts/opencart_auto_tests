from selenium.webdriver.common.by import By

from core.locators import Locators


class RegistrationLocators(Locators):
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM = (By.ID, "input-confirm")
    REG_BUTTON = (By.LINK_TEXT, "Register")
    CHECKBOX_AGREE = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')
    SUBMIT_TEXT = (By.TAG_NAME, "h1")
