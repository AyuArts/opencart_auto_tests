from selenium.webdriver.common.action_chains import ActionChains
from core.web_driver import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from config import settings


class BaseTest:
    def setup_method(self, method):
        self.driver = get_driver()
        self.driver.maximize_window()
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, timeout=settings.default.timeout)

    def teardown_method(self, method):
        if not settings.debug:
            self.driver.quit()

    def open_page(self, url=settings.default.url):
        self.driver.get(url)

    def click(self, by, locator):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def cursor_guidance(self, by, locator):
        element = self.find_element(by, locator)
        self.actions.move_to_element(element).perform()

    def fill_fields(self, by, fields: dict[str, str]):
        for field_id, value in fields.items():
            element = self.find_element(by, field_id)
            element.clear()
            element.send_keys(value)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def select(self, by, field_id):
        element = self.find_element(by, field_id)
        return Select(element)

    def select_by_visible_text(self, by, field_id, text):
        self.select(by, field_id).select_by_visible_text(text)

    def first_selected(self, by, field_id):
        return self.select(by, field_id).first_selected_option

    def execute_script(self, script, **kwargs):
        self.driver.execute_script(script, **kwargs)

    def get_text(self, by, locator):
        element = self.find_element(by, locator)
        return element.text

    def click_and_wait_for_url(self, by, locator, url_contains):
        try:
            self.click(by, locator)
            self.wait.until(EC.url_contains(url_contains))
            return True
        except TimeoutException:
            raise TimeoutException(
                f"The element '{locator}' is not clickable or URL does not contain '{url_contains}' for {settings.default.timeout} seconds."
            )

    def get_elements(self, by, locator):
        try:
            elements = self.wait.until(
                EC.presence_of_all_elements_located((by, locator))
            )
            return [elem.text.strip() for elem in elements if elem.text.strip()]
        except TimeoutException:
            raise TimeoutException(
                f"Elements according to the locator ({by}, '{locator}') were not found for {settings.default.timeout} seconds."
            )
