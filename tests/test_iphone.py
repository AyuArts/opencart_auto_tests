import allure
from core import BaseTest
from core import Logger
from page import Iphone
from page import Main

log = Logger().get_logger("Test_Iphone")


@allure.feature("iPhone product page")
class TestIphonePage(BaseTest):
    """
    UI tests for verifying currency and price display on the iPhone product page
    under different currency settings on the main page.
    """

    def setup_method(self, method):
        super().setup_method(method)
        self.page = Iphone(self.driver, self.wait)
        self.main_page = Main(self.driver, self.wait)

    @allure.title("Verify default currency on the main page is '$'")
    @allure.story("Check that the currency symbol on the main page is '$'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_currency_on_main_page(self):
        """
        Test Steps:
        1. Open the homepage.
        2. Verify that the default currency displayed is '$'.

        Assertion:
        The currency symbol should match the expected value '$'.
        """
        currency = "$"

        with allure.step("Step 1: Check currency symbol on the main page"):
            log.info(f"Verifying currency symbol is '{currency}' on the homepage.")
            assert self.main_page.check_currency(
                currency
            ), f"Currency mismatch. Expected: '{currency}'"

    @allure.title("Verify iPhone price in default currency ($)")
    @allure.story("Check that the iPhone product price is correct in USD")
    @allure.severity(allure.severity_level.NORMAL)
    def test_price_of_product(self):
        """
        Test Steps:
        1. Open the iPhone product page.
        2. Verify that the price displayed is '$123.20'.

        Assertion:
        The displayed price should match the expected value.
        """
        price = "$123.20"

        with allure.step("Step 1: Open the iPhone product page"):
            log.info("Opening iPhone product page.")
            self.page.open_page()

        with allure.step(f"Step 2: Verify product price is '{price}'"):
            log.info(f"Checking iPhone price is '{price}'.")
            assert self.page.check_price_product(
                price
            ), f"Price mismatch. Expected: '{price}'"

    @allure.title("Verify iPhone price after switching currency to Euro")
    @allure.story("Check price update after changing currency to Euro")
    @allure.severity(allure.severity_level.NORMAL)
    def test_price_of_product_after_switch_currency_to_euro(self):
        """
        Test Steps:
        1. Open the iPhone product page.
        2. Switch currency to Euro on the main page.
        3. Verify the price changes to '96.66€'.

        Assertion:
        The displayed price should match the expected Euro value.
        """
        price = "96.66€"

        with allure.step("Step 1: Open the iPhone product page"):
            log.info("Opening iPhone product page.")
            self.page.open_page()

        with allure.step("Step 2: Switch currency to Euro"):
            log.info("Switching currency to Euro.")
            self.main_page.switch_currency_to_euro()

        with allure.step(f"Step 3: Verify product price is '{price}'"):
            log.info(f"Checking iPhone price after switching to Euro: '{price}'.")
            assert self.page.check_price_product(
                price
            ), f"Euro price mismatch. Expected: '{price}'"

    @allure.title("Verify iPhone price after switching currency to Pound Sterling")
    @allure.story("Check price update after changing currency to GBP")
    @allure.severity(allure.severity_level.NORMAL)
    def test_price_of_product_after_switch_currency_to_pound(self):
        """
        Test Steps:
        1. Open the iPhone product page.
        2. Switch currency to Pound Sterling on the main page.
        3. Verify the price changes to '£75.46'.

        Assertion:
        The displayed price should match the expected Pound value.
        """
        price = "£75.46"

        with allure.step("Step 1: Open the iPhone product page"):
            log.info("Opening iPhone product page.")
            self.page.open_page()

        with allure.step("Step 2: Switch currency to Pound Sterling"):
            log.info("Switching currency to Pound Sterling.")
            self.main_page.switch_currency_to_pound()

        with allure.step(f"Step 3: Verify product price is '{price}'"):
            log.info(f"Checking iPhone price after switching to Pound: '{price}'.")
            assert self.page.check_price_product(
                price
            ), f"Pound price mismatch. Expected: '{price}'"
