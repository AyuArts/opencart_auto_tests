import allure
import pytest
from core.base_test import BaseTest
from config import settings
from selenium.webdriver.common.by import By
from core.logger import Logger
from core.utils import is_sorted_ascending

log = Logger().get_logger("Test_three")


@allure.feature("Product sort")
@allure.story(
    "Verify sorting, 'Name (A - Z)' and 'Price (Low > High)' in product catalog"
)
@allure.severity(allure.severity_level.CRITICAL)
class TestThree(BaseTest):
    """
    UI test to verify sorting, 'Name (A - Z)' and 'Price (Low > High)'
    in the product listing page.
    """

    @allure.title(
        "Verification of two product sorting filters: filter first: 'Name (A - Z)' filter second: 'Price (Low > High)'"
    )
    def test_three(self):
        """
        Test Steps:
        1. Hower over Desktops from top menu
        2. Click on Show All Desktops
        3. Select 'Name (A - Z)' from Sort by dropdown
        4. Check that products were sorted correctly
        5. Select 'Price (Low > High)' from Sort by dropdown
        6. Check that products were sorted correctly
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

        with allure.step("Step 3: We get the names of products'"):
            filter_sort = "Name (A - Z)"
            log.info(f"Changing 'Sort' to: {filter_sort}")
            self.select_by_visible_text(
                By.ID, settings.tests.two.input_sort_id, filter_sort
            )
            elements = self.find_elements(By.TAG_NAME, "h4")
            products = [el.text.lower() for el in elements]
            log.info(f"Product names found: {products}")

        with allure.step(
            "Step 4: Verification of product sorting filter: 'Name (A - Z)'"
        ):
            assert is_sorted_ascending(products), "Products are not sorted A-Z"

        with allure.step("Step 5: We get the prices of products"):
            filter_sort = "Price (Low > High)"
            log.info(f"Changing 'Sort' to: {filter_sort}")
            self.select_by_visible_text(
                By.ID, settings.tests.two.input_sort_id, filter_sort
            )
            elements = self.find_elements(By.CLASS_NAME, "price-new")
            products_price = [
                float(el.text.replace("$", "").strip()) for el in elements
            ]
            log.info(f"Product price found: {products_price}")

        with allure.step(
            "Step 6: Verification of product sorting filter: 'Price (Low > High)'"
        ):
            assert is_sorted_ascending(
                products_price
            ), "Products are not sorted Low > High"
