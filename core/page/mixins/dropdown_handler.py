import allure
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class DropdownHandler:
    @allure.step("Select_{text} from dropdown: {locator}")
    def _select(self, locator, text):
        self.log.info(f"Selecting '{text}' in dropdown: {locator}")
        dropdown = Select(self._wait.until(EC.presence_of_element_located(locator)))
        dropdown.select_by_visible_text(text)

    @allure.step("Get first selected option from dropdown: {locator}")
    def _get_first_selected_option(self, locator):
        self.log.info(f"Getting first selected option from dropdown: {locator}")
        dropdown = Select(self._wait.until(EC.presence_of_element_located(locator)))
        return dropdown.first_selected_option.text

    def _switch_to_dropdown(
        self, locator_dropdown, locator_value, locator_wait, wait_value
    ):
        self._click(locator_dropdown)
        self._click(locator_value)
        self._wait_switch(locator_wait, wait_value)

    def _wait_switch(self, locator, value: str):
        self.log.info(f"Waiting for element {locator} to contain text: {value}")
        self._wait.until(EC.text_to_be_present_in_element(locator, value))
