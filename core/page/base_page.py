from abc import ABC, abstractmethod
from selenium.webdriver import ActionChains
from core.scripts import JavaScripts as JS
from locators import BaseLocators as BL

from core.logger import Logger

from .mixins import (
    Clicker,
    DropdownHandler,
    ElementFinder,
    ScriptExecutor,
    TextHandler,
    FieldFiller,
    Checks,
)


class BasePage(
    Clicker,
    DropdownHandler,
    ElementFinder,
    ScriptExecutor,
    TextHandler,
    FieldFiller,
    Checks,
    ABC,
):
    def __init__(self, driver, wait):
        self._driver = driver
        self._wait = wait
        self.log = Logger().get_logger(__name__)
        self._actions = ActionChains(driver)

    @abstractmethod
    def open_page(self):
        pass

    def _cursor_guidance(self, locator):
        self.log.info(f"Moving cursor to element: {locator}")
        element = self._find_element(locator)
        self._actions.move_to_element(element).perform()

    def scroll_down_page(self):
        self.log.info(f"Scrolling down page")
        self._execute_script(JS.SCROLL_TO_DOWN_PAGE_JS)

    def check_currency(self, currency):
        self.log.info(f"Checking currency: {currency}")
        return self._check_text(BL.CURRENCY, currency)

    def switch_currency_to_euro(self, wait_currency="€"):
        self.log.info(f"Switching currency to euro")
        self._switch_to_dropdown(
            locator_dropdown=BL.CURRENCY_DD,
            locator_value=BL.CURRENCY_EURO,
            locator_wait=BL.CURRENCY,
            wait_value=wait_currency,
        )

    def switch_currency_to_pound(self, wait_currency="£"):
        self.log.info(f"Switching currency to pound")
        self._switch_to_dropdown(
            locator_dropdown=BL.CURRENCY_DD,
            locator_value=BL.CURRENCY_POUND,
            locator_wait=BL.CURRENCY,
            wait_value=wait_currency,
        )
