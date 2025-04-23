import allure
from core import BaseTest
from core import Logger
from page import Brands

log = Logger().get_logger("Test_Brands")


@allure.feature("Brands page")
class TestBrandsPage(BaseTest):
    """
    UI test for verifying that the 'Brands' page displays
    the correct list of expected brand names.
    """

    def setup_method(self, method):
        super().setup_method(method)
        self.page = Brands(self.driver, self.wait)

    @allure.title("Verify expected brands are listed on the Brands page")
    @allure.story("Verify default brand names are displayed on the Brands page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_brands(self):
        """
        Test Steps:
        1. Open the 'Brands' page from the homepage.
        2. Retrieve the list of displayed brand names.
        3. Assert that all expected brand names are present on the page.
        """
        expected_brands = ("Apple", "Canon", "Hewlett-Packard", "HTC", "Palm", "Sony")

        with allure.step("Step 1: Open the 'Brands' page"):
            log.info("Opening 'Brands' page via navigation.")
            self.page.open_page()
            log.info("'Brands' page opened successfully.")

        with allure.step("Step 2: Retrieve displayed brand names"):
            log.info("Retrieving brand names from the page.")
            brand_names = self.page.get_brands()
            log.info(f"Displayed brands: {brand_names}")

        with allure.step("Step 3: Verify all expected brand names are present"):
            log.info("Verifying expected brand names are present.")
            for brand in expected_brands:
                assert brand in brand_names, f"Brand '{brand}' not found on the page"
                log.info(f"✔ Brand '{brand}' found on the page.")
