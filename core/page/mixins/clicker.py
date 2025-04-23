import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import settings


class Clicker:
    @allure.step("Click on element: {locator}")
    def _click(self, locator):
        self.log.info(f"Clicking on element: {locator}")
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step(
        "Click on {locator} and wait for URL to contain: {expected_url_substring}"
    )
    def _click_and_wait_for_url(self, locator, expected_url_substring):
        self._click(locator)
        self.log.info(f"Waiting for URL to contain: {expected_url_substring}")
        try:
            self._wait.until(EC.url_contains(expected_url_substring))
        except TimeoutException:
            msg = f"URL did not contain '{expected_url_substring}' within {settings.default.timeout} seconds"
            self.log.error(msg)
            raise TimeoutException(msg)
