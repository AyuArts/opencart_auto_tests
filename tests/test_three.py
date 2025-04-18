import allure
import pytest
from core.base_test import BaseTest
from config import settings
from selenium.webdriver.common.by import By
from core.logger import Logger

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
        1. Open the homepage
        2. Hower over Desktops from top menu
        3. Click on Show All Desktops
        4. Select 'Name (A - Z)' from Sort by dropdown
        5. Check that products were sorted correctly
        6. Select 'Price (Low > High)' from Sort by dropdown
        7. Check that products were sorted correctly
        """

        pass