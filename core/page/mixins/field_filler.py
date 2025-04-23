import allure


class FieldFiller:
    @allure.step("Fill field {locator} with value: {value}")
    def _fill_fields(self, locator, value):
        self.log.info(f"Filling field {locator} with value: {value}")
        field = self._find_element(locator)
        field.clear()
        field.send_keys(value)
