import allure
import pytest
from core.base_test import BaseTest
from config import settings
from selenium.webdriver.common.by import By
from core.logger import Logger

log = Logger().get_logger("Test_two")


@allure.feature("Product listing")
@allure.story("Verify sorting, limits and pagination in product catalog")
@allure.severity(allure.severity_level.CRITICAL)
class TestTwo(BaseTest):
    """
    UI test to verify default sorting, pagination,
    and layout behavior in the product listing page.
    """

    @allure.title("Verify product listing default filters, limit change and pagination")
    def test_two(self):
        """
        Test Steps:
        1. Hover over the dropdown menu
        2. Click on the section button
        3. Verify default selected limit and sorting
        4. Verify number of displayed products
        5. Change limit value and verify change
        6. Verify pagination content
        7. Scroll and verify pagination visibility
        """
        with allure.step("Step 1: Hover over the dropdown menu"):
            log.info(f"Hovering over dropdown: {settings.tests.two.dropdown}")
            self.cursor_guidance(
                By.LINK_TEXT,
                settings.tests.two.dropdown,
            )

        with allure.step("Step 2: Click on the catalog section"):
            log.info(f"Clicking button: {settings.tests.two.button_text}")
            self.click(
                By.LINK_TEXT,
                settings.tests.two.button_text,
            )

        with allure.step(
            "Step 3: Verify default selected values for 'Show' and 'Sort By' dropdowns"
        ):
            show_value = self.first_selected(
                By.ID, settings.tests.two.input_limit_id
            ).text
            sort_value = self.first_selected(
                By.ID, settings.tests.two.input_sort_id
            ).text
            log.info(f"Default 'Show' value: {show_value}")
            log.info(f"Default 'Sort By' value: {sort_value}")
            assert (
                show_value == settings.tests.two.input_limit_value_def
            ), f"Expected default 'Show' value: {settings.tests.two.input_limit_value_def}, got: {show_value}"
            assert (
                sort_value == settings.tests.two.input_sort_value_def
            ), f"Expected default 'Sort By' value: {settings.tests.two.input_sort_value_def}, got: {sort_value}"

        with allure.step("Step 4: Verify number of displayed products"):
            products = self.find_elements(
                By.CLASS_NAME, settings.tests.two.product_layout
            )
            log.info(f"Number of displayed products: {len(products)}")
            assert (
                len(products) == settings.tests.two.product_count
            ), f"Expected {settings.tests.two.product_count} products, found {len(products)}"

        with allure.step("Step 5: Change 'Show' limit and verify update"):
            log.info(
                f"Changing 'Show' limit to: {settings.tests.two.input_limit_value_new}"
            )
            self.select_by_visible_text(
                By.ID,
                settings.tests.two.input_limit_id,
                settings.tests.two.input_limit_value_new,
            )
            new_show_value = self.first_selected(
                By.ID, settings.tests.two.input_limit_id
            ).text
            log.info(f"New 'Show' value: {new_show_value}")
            assert (
                new_show_value == settings.tests.two.input_limit_value_new
            ), f"Expected new 'Show' value: {settings.tests.two.input_limit_value_new}, got: {new_show_value}"

        with allure.step("Step 6: Verify pagination text matches expected"):
            pagination = self.find_element(
                By.CSS_SELECTOR, settings.tests.two.pagination_selector
            )
            log.info(f"Pagination text: {pagination.text}")
            assert (
                pagination.text == settings.tests.two.pagination_text_expected
            ), f"Expected pagination text: '{settings.tests.two.pagination_text_expected}', got: '{pagination.text}'"

        with allure.step("Step 7: Scroll and verify pagination is visible"):
            log.info("Executing scroll script to bring pagination into view.")
            self.execute_script(settings.tests.two.script_scroll)
            assert (
                pagination.is_displayed()
            ), "Pagination element is not visible after scroll"
            log.info("Pagination is visible after scroll.")
