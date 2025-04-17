from selenium.webdriver.common.by import By

from core.web_driver import driver as dr
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest:
    def setup_method(self, method):
        if not settings.default.debug:
            self.driver = dr
            self.driver.maximize_window()
        else:
            options = Options()
            self.driver = webdriver.Chrome(options=options)
            self.driver.maximize_window()

    def teardown_method(self, method):
        if not settings.default.debug:
            self.driver.quit()

    def open_page(self, url=settings.default.url):
        self.driver.get(url)

    def click(self, by, locator, timeout=settings.default.timeout):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def fill_fields(self, by, fields: dict[str, str]):
        for field_id, value in fields.items():
            element = self.driver.find_element(by, field_id)
            element.clear()
            element.send_keys(value)

    def get_text(self, by, locator):
        element = self.driver.find_element(by, locator)
        return element.text

    def click_and_wait_for_url(
        self, by, locator, url_contains, timeout=settings.default.timeout
    ):
        wait = WebDriverWait(self.driver, timeout)
        try:
            self.click(by, locator, timeout=timeout)
            wait.until(EC.url_contains(url_contains))
            return True
        except TimeoutException:
            raise TimeoutException(
                f"The element '{locator}' is not clickable or URL does not contain '{url_contains}' for {timeout} seconds."
            )

    def get_elements(self, by, locator, timeout=settings.default.timeout):
        wait = WebDriverWait(self.driver, timeout)
        try:
            elements = wait.until(EC.presence_of_all_elements_located((by, locator)))
            return [elem.text.strip() for elem in elements if elem.text.strip()]
        except TimeoutException:
            raise TimeoutException(
                f"Elements according to the locator ({by}, '{locator}') were not found for {timeout} seconds."
            )
