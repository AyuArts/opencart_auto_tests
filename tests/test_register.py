import allure
from core import BaseTest
from core import Logger
from page import Registration
from utils.random_user import user

log = Logger().get_logger("Test_Register")


@allure.feature("Register page")
class TestRegisterPage(BaseTest):
    """
    UI test for verifying that the 'Register' page allows valid user registration.
    """

    def setup_method(self, method):
        super().setup_method(method)
        self.page = Registration(self.driver, self.wait)

    @allure.title("Valid user can register on the 'Register' page")
    @allure.story("Successful registration with valid data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_register(self):
        """
        Test Steps:
        1. Open the 'Register' page from the homepage.
        2. Fill in the registration form with valid data.
        3. Submit the registration form.
        4. Verify successful registration.
        """
        with allure.step("Step 1: Open the 'Register' page"):
            log.info("Opening 'Register' page via navigation.")
            self.page.open_page()
            log.info("'Register' page opened successfully.")

        with allure.step("Step 2: Fill in the registration form"):
            log.info("Filling in registration form with valid user data.")
            self.page.fill_register_form(
                firstName=user.first_name,
                lastName=user.last_name,
                email=user.email,
                telephone=user.phone,
                password=user.password,
                confirm=user.password,
            )

        with allure.step("Step 3: Submit the form"):
            log.info("Submitting the registration form.")
            self.page.confirm_form()

        with allure.step("Step 4: Verify registration is successful"):
            log.info("Verifying successful registration.")
            text_expected: str = "Your Account Has Been Created!"
            assert self.page.check_register(
                text_expected
            ), "Registration failed or was not confirmed properly."
