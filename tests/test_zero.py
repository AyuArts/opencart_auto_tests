import allure
from selenium.webdriver.common.by import By
from core.base_test import BaseTest
from config import settings
from core.logger import Logger


log = Logger().get_logger("Test_zero")


@allure.feature("Brands section")
@allure.story("Verify default brand names are displayed on the Brands page")
@allure.severity(allure.severity_level.CRITICAL)
class TestZero(BaseTest):
    """
    UI test to verify that all expected brand names are shown
    on the 'Brands' page accessed from the homepage.
    """

    @allure.title("Verify expected brands are listed on the Brands page")
    def test_brands(self):
        """
        Test Steps:
        1. Click on the 'Brands' link
        2. Retrieve brand names from the page
        3. Assert that all expected brands are present
        """
        with allure.step(
            "Step 1: Click on the 'Brands' link at the bottom of the page"
        ):
            log.info("Clicking on the 'Brands' link.")
            self.click_and_wait_for_url(
                by=By.LINK_TEXT,
                locator="Brands",
                url_contains=settings.tests.zero.url_contains,
            )
            log.info("Navigation to Brands page successful.")

        with allure.step("Step 2: Retrieve the list of displayed brand names"):
            log.info("Retrieving brand names from the page.")
            brand_names = self.get_elements(
                By.CSS_SELECTOR, settings.tests.zero.css_selector
            )
            log.info(f"Found brand names: {brand_names}")

        with allure.step("Step 3: Verify all expected brand names are present"):
            log.info("Verifying expected brand names are on the page.")
            for brand in settings.tests.zero.expected_brands:
                assert brand in brand_names, f"Brand '{brand}' not found on the page"
                log.info(f"Brand '{brand}' is present.")
