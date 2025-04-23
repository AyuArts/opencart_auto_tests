import allure
from selenium.webdriver.support import expected_conditions as EC


class ElementFinder:
    @allure.step("Find element: {locator}")
    def _find_element(self, locator):
        self.log.info(f"Finding element: {locator}")
        return self._wait.until(EC.presence_of_element_located(locator))

    @allure.step("Find all elements: {locator}")
    def _find_elements(self, locator):
        self.log.info(f"Finding all elements: {locator}")
        return self._wait.until(EC.presence_of_all_elements_located(locator))
