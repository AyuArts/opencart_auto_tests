import allure

from selenium.webdriver.support.ui import WebDriverWait

from core.web_driver import get_driver
from config import settings


from core import Logger

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
            self.wait = WebDriverWait(self.driver, timeout=settings.default.timeout)
            log.info("WebDriver initialized and window maximized.")
            log.info("Opening homepage.")
            self._open_project()
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

    @allure.step("open project: {url}")
    def _open_project(self, url: str = settings.default.url):
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
