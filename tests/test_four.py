import allure
import pytest
from core.base_test import BaseTest
from config import settings
from selenium.webdriver.common.by import By
from core.logger import Logger

log = Logger().get_logger("TestFour")


@allure.feature("Currency Verification")
@allure.story("Check product price in different currencies")
@allure.severity(allure.severity_level.CRITICAL)
class TestFour(BaseTest):
    """
    UI test to verify that the product price updates correctly when changing the currency on the homepage.

    Test Steps:
    1. Verify that the current currency is Dollar ($), and change it if necessary.
    2. Navigate to the iPhone product page.
    3. Verify that the price is $123.20.
    4. Change the currency to Euro (€).
    5. Verify that the price is €96.66
    6. Change the currency to Pound Sterling (£).
    7. Verify that the price is £75.46
    """

    @allure.title("Verify product price updates when changing currencies")
    def test_four(self):
        with allure.step(
            "Step 1: Check that current currency is '$' and change if not"
        ):
            assert self.find_element(By.TAG_NAME, "strong").text == "$"
            log.info("Checking if current currency is '$'.")

        with allure.step("Step 2: Navigate to the iPhone product page"):
            assert self.click_and_wait_for_url(
                By.XPATH,
                locator='//*[@id="content"]/div[2]/div[2]/div/div[1]/a/img',
                url_contains="route=product/product&product_id=40",
            )
            log.info("Navigating to the iPhone product page.")

        with allure.step("Step 3: Verify that the price is $123.20"):
            assert (
                self.find_element(
                    By.XPATH, locator='//*[@id="content"]/div[1]/div[2]/ul[2]/li[1]/h2'
                ).text
                == "$123.20"
            )
            log.info("Verifying that the price is $123.20.")

        with allure.step("Step 4: Change currency to Euro (€)"):
            self.click(By.CLASS_NAME, locator="fa-caret-down")
            self.click(By.NAME, locator="EUR")
            assert self.find_element(By.TAG_NAME, "strong").text == "€"
            log.info("Changing currency to Euro (€).")

        with allure.step("Step 5: Verify that the price is €96.66"):
            assert (
                self.find_element(
                    By.XPATH, locator='//*[@id="content"]/div[1]/div[2]/ul[2]/li[1]/h2'
                ).text
                == "96.66€"
            )
            log.info("Verifying that the price is €96.66.")

        with allure.step("Step 6: Change currency to Pound Sterling (£)"):
            self.click(By.CLASS_NAME, locator="fa-caret-down")
            self.click(By.NAME, locator="GBP")
            assert self.find_element(By.TAG_NAME, "strong").text == "£"
            log.info("Changing currency to Pound Sterling (£).")

        with allure.step("Step 7: Verify that the price is £75.46"):
            assert (
                self.find_element(
                    By.XPATH, locator='//*[@id="content"]/div[1]/div[2]/ul[2]/li[1]/h2'
                ).text
                == "£75.46"
            )
            log.info("Verifying that the price is £75.46.")
