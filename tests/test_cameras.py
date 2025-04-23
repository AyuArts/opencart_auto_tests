import allure
from core import BaseTest
from core import Logger
from page import Cameras

log = Logger().get_logger("Test_Cameras")


@allure.feature("Cameras page")
class TestCamerasPage(BaseTest):
    """
    UI tests for validating product count and prices
    (new, old, tax) on the 'Cameras' category page.
    """

    def setup_method(self, method):
        super().setup_method(method)
        self.page = Cameras(self.driver, self.wait)

    @allure.title("Verify number of camera products on the page")
    @allure.story("Check that 2 products are displayed in the 'Cameras' category")
    @allure.severity(allure.severity_level.NORMAL)
    def test_exist_product(self):
        """
        Test Steps:
        1. Open the 'Cameras' category page.
        2. Verify that 2 products are displayed.

        Assertion:
        Product count should be exactly 2.
        """
        count_products = 2

        with allure.step("Step 1: Open the 'Cameras' page"):
            log.info("Opening 'Cameras' category page.")
            self.page.open_page()

        with allure.step("Step 2: Check number of displayed products"):
            log.info(f"Verifying product count equals {count_products}.")
            assert self.page.check_count_products(
                count_products
            ), f"Expected {count_products} products, but found a different number."

    @allure.title("Verify new price for 'Canon EOS 5D'")
    @allure.story("Check that the new price is displayed correctly for 'Canon EOS 5D'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_price_new(self):
        """
        Test Steps:
        1. Open the 'Cameras' category page.
        2. Verify the new price of 'Canon EOS 5D' is $98.00.

        Assertion:
        The displayed new price should match the expected value.
        """
        product_name = "Canon EOS 5D"
        method_price = "new"
        price = "$98.00"

        with allure.step("Step 1: Open the 'Cameras' page"):
            log.info("Opening 'Cameras' category page.")
            self.page.open_page()

        with allure.step("Step 2: Verify new price for product"):
            log.info(f"Verifying new price for '{product_name}' is '{price}'.")
            assert self.page.check_price_current_product(
                name_product=product_name, method_price=method_price, price=price
            ), f"New price for '{product_name}' does not match expected value: {price}"

    @allure.title("Verify old price for 'Canon EOS 5D'")
    @allure.story("Check that the old price is displayed correctly for 'Canon EOS 5D'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_price_old(self):
        """
        Test Steps:
        1. Open the 'Cameras' category page.
        2. Verify the old price of 'Canon EOS 5D' is $122.00.

        Assertion:
        The displayed old price should match the expected value.
        """
        product_name = "Canon EOS 5D"
        method_price = "old"
        price = "$122.00"

        with allure.step("Step 1: Open the 'Cameras' page"):
            log.info("Opening 'Cameras' category page.")
            self.page.open_page()

        with allure.step("Step 2: Verify old price for product"):
            log.info(f"Verifying old price for '{product_name}' is '{price}'.")
            assert self.page.check_price_current_product(
                name_product=product_name, method_price=method_price, price=price
            ), f"Old price for '{product_name}' does not match expected value: {price}"

    @allure.title("Verify tax price for 'Nikon D300'")
    @allure.story("Check that the tax price is displayed correctly for 'Nikon D300'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_price_tax(self):
        """
        Test Steps:
        1. Open the 'Cameras' category page.
        2. Verify the tax price of 'Nikon D300' is $80.00.

        Assertion:
        The displayed tax price should match the expected value.
        """
        product_name = "Nikon D300"
        method_price = "tax"
        price = "$80.00"

        with allure.step("Step 1: Open the 'Cameras' page"):
            log.info("Opening 'Cameras' category page.")
            self.page.open_page()

        with allure.step("Step 2: Verify tax price for product"):
            log.info(f"Verifying tax price for '{product_name}' is '{price}'.")
            assert self.page.check_price_current_product(
                name_product=product_name, method_price=method_price, price=price
            ), f"Tax price for '{product_name}' does not match expected value: {price}"
