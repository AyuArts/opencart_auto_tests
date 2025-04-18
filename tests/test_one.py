import allure
import pytest
from core.base_test import BaseTest
from config import settings
from selenium.webdriver.common.by import By
from core.logger import Logger

log = Logger().get_logger("Test_one")


@allure.feature("Registration")
@allure.story("Complete user registration with valid data")
@allure.severity(allure.severity_level.BLOCKER)
class TestOne(BaseTest):
    """
    UI test to validate the full registration process with valid user data.
    """

    @allure.title("Register a new user with valid data and verify success message")
    def test_one(self):
        """
        Test Steps:
        1. Open homepage
        2. Click on dropdown menu
        3. Navigate to registration page
        4. Fill in registration fields
        5. Accept terms checkbox
        6. Submit registration form
        7. Verify success message
        """
        with allure.step("Step 1: Open the homepage"):
            log.info("Opening homepage.")
            self.open_page()
            log.info("Homepage opened successfully.")

        with allure.step("Step 2: Click on dropdown menu"):
            log.info("Clicking dropdown element.")
            self.click(by=By.XPATH, locator=settings.tests.one.dropdown)
            log.info("Dropdown menu clicked.")

        with allure.step("Step 3: Navigate to registration page"):
            log.info("Clicking registration element and waiting for URL change.")
            self.click_and_wait_for_url(
                by=By.XPATH,
                locator=settings.tests.one.element_reg,
                url_contains=settings.tests.one.url_reg,
            )
            log.info("Navigated to registration page.")

        with allure.step("Step 4: Fill in registration form fields"):
            log.info(f"Filling registration fields: {settings.tests.one.fields_regs}")
            self.fill_fields(by=By.ID, fields=settings.tests.one.fields_regs)

        with allure.step("Step 5: Accept terms and conditions checkbox"):
            log.info("Clicking checkbox to accept terms.")
            self.click(by=By.XPATH, locator=settings.tests.one.check_box)

        with allure.step("Step 6: Submit the registration form"):
            log.info("Clicking continue button and waiting for confirmation page.")
            self.click_and_wait_for_url(
                by=By.XPATH,
                locator=settings.tests.one.button_continue,
                url_contains=settings.tests.one.url_approve_reg,
            )
            log.info("Submitted registration form.")

        with allure.step("Step 7: Verify success message is displayed"):
            log.info("Retrieving and verifying confirmation text.")
            text_correct = self.get_text(
                by=By.TAG_NAME, locator=settings.tests.one.text_correct
            )
            log.info(f"Confirmation text found: {text_correct}")
            assert (
                settings.tests.one.text_expected in text_correct
            ), f"Expected text '{settings.tests.one.text_expected}' not found in '{text_correct}'"
            log.info("Success message verified.")
