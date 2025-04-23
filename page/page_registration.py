from core.page import PageAuth
from locators import RegistrationLocators as PL  # PL - page locators
from locators import BaseLocators as BL
from page.routers import routers as r


class PageRegistration(PageAuth):
    def open_page(self):
        self._click(BL.MY_ACCOUNT_LINK)
        self._click_and_wait_for_url(PL.REG_BUTTON, r.REGISTER_URL)

    def fill_register_form(
        self, firstName, lastName, email, telephone, password, confirm
    ):
        field_data = {
            PL.FIRST_NAME: firstName,
            PL.LAST_NAME: lastName,
            PL.EMAIL: email,
            PL.PHONE: telephone,
            PL.PASSWORD: password,
            PL.CONFIRM: confirm,
        }

        for locator, value in field_data.items():
            self._fill_fields(locator, value)

    def confirm_form(self):
        self._click(PL.CHECKBOX_AGREE)
        self._click_and_wait_for_url(PL.CONTINUE_BUTTON, r.SUBMIT_REGISTER_URL)

    def check_register(self, expected_text):
        current_text = self._get_text(PL.SUBMIT_TEXT)
        return expected_text == current_text
