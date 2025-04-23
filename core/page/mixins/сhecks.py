import re

from more_itertools import pairwise

from config import settings


class Checks:
    def _check_dropdown_select(self, locator, expected_value: str) -> bool:
        actual_value = self._get_first_selected_option(locator)
        self.log.info(f"Dropdown selected: {actual_value}, expected: {expected_value}")
        return actual_value == expected_value

    def _check_count(self, locator, expected_count: int) -> bool:
        actual_count = len(self._find_elements(locator))
        self.log.info(f"Count: {actual_count}, expected: {expected_count}")
        return actual_count == expected_count

    def _check_text_in_elements(self, locator, expected_text: str) -> bool:
        actual_text = self._find_elements(locator).text
        return expected_text == actual_text

    def _check_text(self, locator, expected_text: str) -> bool:
        actual_text = self._find_element(locator).text
        return expected_text == actual_text

    def _check_element_is_displayed(self, locator) -> bool:
        return self._find_element(locator).is_displayed()

    @staticmethod
    def _check_is_sorted_ascending(lst) -> bool:
        return all(a <= b for a, b in pairwise(lst))

    import re

    def _check_float(self, locator, expected_value: str) -> bool:
        """
        Check that the float number from the element's text matches the expected float value.

        :param locator: Tuple[By, str] – the locator for the target element.
        :param expected_value: str – a string containing expected float, e.g. "$98.00".
        :return: True if floats match, otherwise False.
        """
        actual_text = self._find_element(locator).text
        actual_match = re.search(settings.reg.float, actual_text)
        expected_match = re.search(settings.reg.float, expected_value)

        if not actual_match or not expected_match:
            self.log.warning(
                f"Float value not found: actual='{actual_text}', expected='{expected_value}'"
            )
            return False

        actual_float = float(actual_match.group())
        expected_float = float(expected_match.group())

        self.log.info(
            f"Comparing floats: actual={actual_float}, expected={expected_float}"
        )
        return actual_float == expected_float
