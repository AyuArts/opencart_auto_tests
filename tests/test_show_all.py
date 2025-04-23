import allure
from core import BaseTest
from core import Logger
from page import ShowAll

log = Logger().get_logger("Test_ShowAll")


@allure.feature("ShowAll page")
class TestShowAllPage(BaseTest):
    """
    UI tests for verifying dropdown filters, sorting, pagination,
    and product order on the 'Show All' page of the OpenCart site.
    """

    def setup_method(self, method):
        super().setup_method(method)
        self.page = ShowAll(self.driver, self.wait)

    @allure.title("Verify 'Show' dropdown default value is correct")
    @allure.story("Verify default selected value in the 'Show' dropdown")
    @allure.severity(allure.severity_level.NORMAL)
    def test_value_in_show_dropdown(self):
        """
        Test Steps:
        1. Open the 'Show All' page.
        2. Verify that the default value in the 'Show' dropdown is '20'.

        Assertion:
        The actual dropdown value should match the expected value.
        """
        value_in_show = "20"

        with allure.step("Step 1: Open the 'Show All' page"):
            log.info("Opening 'Show All' page.")
            self.page.open_page()

        with allure.step(
            f"Step 2: Check if 'Show' dropdown has value '{value_in_show}'"
        ):
            log.info(f"Verifying 'Show' dropdown value is '{value_in_show}'.")
            assert self.page.check_filter_in_show(
                value_in_show
            ), f"'Show' dropdown value mismatch. Expected: {value_in_show}"

    @allure.title("Verify 'Sort By' dropdown default value is correct")
    @allure.story("Verify default selected value in the 'Sort By' dropdown")
    @allure.severity(allure.severity_level.NORMAL)
    def test_value_in_sort_dropdown(self):
        """
        Test Steps:
        1. Open the 'Show All' page.
        2. Verify that the default value in the 'Sort By' dropdown is 'Default'.

        Assertion:
        The actual dropdown value should match the expected value.
        """
        value_in_sort = "Default"

        with allure.step("Step 1: Open the 'Show All' page"):
            log.info("Opening 'Show All' page.")
            self.page.open_page()

        with allure.step(
            f"Step 2: Check if 'Sort By' dropdown has value '{value_in_sort}'"
        ):
            log.info(f"Verifying 'Sort By' dropdown value is '{value_in_sort}'.")
            assert self.page.check_filter_in_sort_by(
                value_in_sort
            ), f"'Sort By' dropdown value mismatch. Expected: {value_in_sort}"

    @allure.title("Verify number of displayed products")
    @allure.story("Validate correct product count after opening the page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_count_products(self):
        """
        Test Steps:
        1. Open the 'Show All' page.
        2. Count the number of displayed product blocks.

        Assertion:
        The count of products should equal the expected number (12).
        """
        count_products = 12

        with allure.step("Step 1: Open the 'Show All' page"):
            log.info("Opening 'Show All' page.")
            self.page.open_page()

        with allure.step(f"Step 2: Verify product count equals {count_products}"):
            log.info(f"Checking product count is {count_products}.")
            assert self.page.check_count_products(
                count_products
            ), f"Product count mismatch. Expected: {count_products}"

    @allure.title("Switch 'Show' value and verify changes")
    @allure.story("Change value in the 'Show' dropdown and validate result")
    @allure.severity(allure.severity_level.NORMAL)
    def test_switch_show(self):
        """
        Test Steps:
        1. Open the 'Show All' page.
        2. Switch the 'Show' dropdown value to '25'.
        3. Verify the new selected value and product count.

        Assertion:
        The 'Show' dropdown should reflect the new value, and product count should match expectation.
        """
        option_sort = "25"
        expected_count = 12

        with allure.step("Step 1: Open the 'Show All' page"):
            log.info("Opening 'Show All' page.")
            self.page.open_page()

        with allure.step(f"Step 2: Change 'Show' dropdown to '{option_sort}'"):
            log.info(f"Switching 'Show' dropdown to '{option_sort}'.")
            self.page.switch_filter_show(option_sort)

        with allure.step("Step 3: Validate new 'Show' value and product count"):
            log.info("Verifying new 'Show' value and product count.")
            assert self.page.check_filter_in_show(
                option_sort
            ), f"'Show' value mismatch after switching. Expected: {option_sort}"
            assert self.page.check_count_products(
                expected_count
            ), f"Product count mismatch after switching 'Show'. Expected: {expected_count}"

    @allure.title("Verify pagination text is correct")
    @allure.story("Check that pagination displays expected text")
    @allure.severity(allure.severity_level.MINOR)
    def test_pagination_text_valid(self):
        """
        Test Steps:
        1. Open the 'Show All' page.
        2. Verify that the pagination text is correct.

        Assertion:
        The displayed pagination text should exactly match the expected string.
        """
        pagination_text = "Showing 1 to 12 of 12 (1 Pages)"

        with allure.step("Step 1: Open the 'Show All' page"):
            log.info("Opening 'Show All' page.")
            self.page.open_page()

        with allure.step(
            f"Step 2: Validate pagination text equals '{pagination_text}'"
        ):
            log.info(f"Checking pagination text is '{pagination_text}'.")
            assert self.page.check_text_pagination(
                pagination_text
            ), f"Pagination text mismatch. Expected: '{pagination_text}'"

    @allure.title("Verify pagination block is located at the bottom")
    @allure.story("Ensure pagination block is displayed at the bottom of the page")
    @allure.severity(allure.severity_level.MINOR)
    def test_pagination_location_down_page(self):
        """
        Test Steps:
        1. Open the 'Show All' page.
        2. Verify the pagination block is displayed at the bottom of the page.

        Assertion:
        The pagination element should be present and visible.
        """
        with allure.step("Step 1: Open the 'Show All' page"):
            log.info("Opening 'Show All' page.")
            self.page.open_page()

        with allure.step("Step 2: Verify pagination is located at the bottom"):
            log.info("Checking that pagination is located at the bottom of the page.")
            assert (
                self.page.check_pagination_down_page()
            ), "Pagination block is not displayed at the bottom of the page."

    @allure.title("Sort products by name and validate alphabetical order")
    @allure.story("Check alphabetical order after selecting 'Name (A - Z)'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sort_by_alphabet_order(self):
        """
        Test Steps:
        1. Open the 'Show All' page.
        2. Select sorting by 'Name (A - Z)'.
        3. Verify that products are sorted in alphabetical order.

        Assertion:
        The product names should be in ascending alphabetical order.
        """
        option_sort = "Name (A - Z)"

        with allure.step("Step 1: Open the 'Show All' page"):
            log.info("Opening 'Show All' page.")
            self.page.open_page()

        with allure.step(f"Step 2: Select sorting by '{option_sort}'"):
            log.info(f"Selecting sort option '{option_sort}'.")
            self.page.switch_filter_in_sort_by(option_sort)

        with allure.step("Step 3: Validate products are sorted alphabetically"):
            log.info("Verifying alphabetical order of products.")
            assert (
                self.page.check_alphabet_order()
            ), "Product names are not sorted alphabetically as expected."

    @allure.title("Sort products by price and validate price order")
    @allure.story("Check price order after selecting 'Price (Low > High)'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sort_by_price_order(self):
        """
        Test Steps:
        1. Open the 'Show All' page.
        2. Select sorting by 'Price (Low > High)'.
        3. Verify that products are sorted by ascending price.

        Assertion:
        The product prices should be sorted in ascending numerical order.
        """
        option_sort = "Price (Low > High)"

        with allure.step("Step 1: Open the 'Show All' page"):
            log.info("Opening 'Show All' page.")
            self.page.open_page()

        with allure.step(f"Step 2: Select sorting by '{option_sort}'"):
            log.info(f"Selecting sort option '{option_sort}'.")
            self.page.switch_filter_in_sort_by(option_sort)

        with allure.step("Step 3: Validate products are sorted by price ascending"):
            log.info("Verifying price order of products.")
            assert (
                self.page.check_price_order()
            ), "Product prices are not sorted in ascending order as expected."
