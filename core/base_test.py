import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from core.web_driver import get_driver
from config import settings
from selenium.webdriver.common.by import By

from core.logger import Logger

log = Logger().get_logger("Base_test")


class BaseTest:
    """Base class for UI tests with reusable helper methods for Selenium WebDriver."""

    def setup_method(self, method):
        """
        Initialize WebDriver, window, actions, and waits.
        """
        try:
            self.driver = get_driver()
            self.driver.maximize_window()
            self.actions = ActionChains(self.driver)
            self.wait = WebDriverWait(self.driver, timeout=settings.default.timeout)
            log.info("WebDriver initialized and window maximized.")
            log.info("Opening homepage.")
            self.open_page()
            log.info("Homepage opened successfully.")
        except Exception as e:
            log.exception("Error during setup_method: %s", str(e))
            raise

    def teardown_method(self, method):
        """
        Close the WebDriver after test execution.
        """
        try:
            if not settings.debug:
                self.driver.quit()
                log.info("WebDriver closed.")
        except Exception as e:
            log.exception("Error during teardown_method: %s", str(e))
            raise

    @allure.step("Open page: {url}")
    def open_page(self, url=settings.default.url):
        """
        Open a specified URL in the browser.
        :param url: The URL to open.
        """
        try:
            log.info(f"Opening URL: {url}")
            self.driver.get(url)
        except Exception as e:
            log.exception(f"Failed to open URL: {url}")
            raise

    @allure.step("Click on element: {locator}")
    def click(self, by, locator):
        """
        Click on a web element.
        :param by: Selenium By locator strategy.
        :param locator: The locator string.
        """
        try:
            log.info(f"Clicking element: ({by}, {locator})")
            element = self.wait.until(EC.element_to_be_clickable((by, locator)))
            element.click()
        except Exception as e:
            log.exception(f"Failed to click element: ({by}, {locator})")
            raise

    @allure.step("Move cursor to element: {locator}")
    def cursor_guidance(self, by, locator):
        """
        Move mouse cursor to an element.
        """
        try:
            log.info(f"Moving cursor to element: ({by}, {locator})")
            element = self.find_element(by, locator)
            self.actions.move_to_element(element).perform()
        except Exception as e:
            log.exception(f"Failed to move cursor to: ({by}, {locator})")
            raise

    @allure.step("Fill fields: {fields}")
    def fill_fields(self, by, fields: dict[str, str]):
        """
        Fill multiple input fields.
        :param by: Locator strategy.
        :param fields: Dictionary of field locator and value.
        """
        try:
            for field_id, value in fields.items():
                log.info(f"Filling field {field_id} with value '{value}'")
                element = self.find_element(by, field_id)
                element.clear()
                element.send_keys(value)
        except Exception as e:
            log.exception(f"Failed to fill fields: {fields}")
            raise

    def find_element(self, by, locator):
        """
        Find a single web element.
        """
        try:
            log.debug(f"Finding element: ({by}, {locator})")
            return self.driver.find_element(by, locator)
        except NoSuchElementException:
            log.error(f"Element not found: ({by}, {locator})")
            raise

    def find_elements(self, by, locator):
        """
        Find multiple elements.
        """
        try:
            log.debug(f"Finding elements: ({by}, {locator})")
            return self.driver.find_elements(by, locator)
        except NoSuchElementException:
            log.error(f"Elements not found: ({by}, {locator})")
            raise

    def select(self, by, field_id):
        """
        Return Select object for dropdown.
        """
        try:
            log.debug(f"Selecting dropdown: ({by}, {field_id})")
            element = self.find_element(by, field_id)
            return Select(element)
        except Exception as e:
            log.exception(f"Failed to get Select element: ({by}, {field_id})")
            raise

    @allure.step("Select option '{text}' in dropdown: {field_id}")
    def select_by_visible_text(self, by, field_id, text):
        """
        Select a dropdown option by visible text.
        """
        try:
            log.info(f"Selecting option '{text}' in dropdown {field_id}")
            self.select(by, field_id).select_by_visible_text(text)
        except Exception as e:
            log.exception(f"Failed to select '{text}' in dropdown {field_id}")
            raise

    def first_selected(self, by, field_id):
        """
        Get first selected option from dropdown.
        """
        try:
            return self.select(by, field_id).first_selected_option
        except Exception as e:
            log.exception(f"Failed to get first selected option: ({by}, {field_id})")
            raise

    @allure.step("Execute JavaScript: {script}")
    def execute_script(self, script, **kwargs):
        """
        Execute JavaScript in browser.
        """
        try:
            log.info(f"Executing JS script: {script}")
            self.driver.execute_script(script, **kwargs)
        except Exception as e:
            log.exception(f"Failed to execute script: {script}")
            raise

    @allure.step("Get text of element: {locator}")
    def get_text(self, by, locator):
        """
        Get the text content of a web element.
        """
        try:
            log.info(f"Getting text of element: ({by}, {locator})")
            element = self.find_element(by, locator)
            return element.text
        except Exception as e:
            log.exception(f"Failed to get text of element: ({by}, {locator})")
            raise

    @allure.step("Click on '{locator}' and wait for URL to contain: '{url_contains}'")
    def click_and_wait_for_url(self, by, locator, url_contains):
        """
        Click and wait for the URL to change.
        """
        try:
            log.info(
                f"Clicking on element ({by}, {locator}) and waiting for URL to contain '{url_contains}'"
            )
            self.click(by, locator)
            self.wait.until(EC.url_contains(url_contains))
            log.info(f"URL contains '{url_contains}'")
            return True
        except TimeoutException as e:
            msg = f"Element '{locator}' or URL did not match expected content within {settings.default.timeout} seconds."
            log.error(msg)
            raise TimeoutException(msg)

    @allure.step("Get all text elements by locator: {locator}")
    def get_elements(self, by, locator):
        """
        Get visible texts of all matched elements.
        """
        try:
            log.info(f"Getting all text elements for locator: ({by}, {locator})")
            elements = self.wait.until(
                EC.presence_of_all_elements_located((by, locator))
            )
            texts = [elem.text.strip() for elem in elements if elem.text.strip()]
            log.debug(f"Extracted texts: {texts}")
            return texts
        except TimeoutException as e:
            msg = f"Elements ({by}, '{locator}') not found within {settings.default.timeout} seconds."
            log.error(msg)
            raise TimeoutException(msg)
