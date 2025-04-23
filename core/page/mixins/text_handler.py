import allure


class TextHandler:
    @allure.step("Get text from element: {locator}")
    def _get_text(self, locator):
        self.log.info(f"Getting text from: {locator}")
        return self._find_element(locator).text

    @allure.step("Get all non-empty texts from elements: {locator}")
    def _get_elements_text(self, locator):
        self.log.info(f"Getting texts from elements: {locator}")
        return [
            el.text.strip() for el in self._find_elements(locator) if el.text.strip()
        ]
