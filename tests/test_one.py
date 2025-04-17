import pytest
from core.base_test import BaseTest
from config import settings
from selenium.webdriver.common.by import By


class TestOne(BaseTest):
    def test_one(self):
        self.open_page()

        self.click(by=By.XPATH, locator=settings.tests.one.dropdown)

        self.click_and_wait_for_url(
            by=By.XPATH,
            locator=settings.tests.one.element_reg,
            url_contains=settings.tests.one.url_reg,
        )

        self.fill_fields(by=By.ID, fields=settings.tests.one.fields_regs)
        self.click(by=By.XPATH, locator=settings.tests.one.check_box)

        self.click_and_wait_for_url(
            by=By.XPATH,
            locator=settings.tests.one.button_continue,
            url_contains=settings.tests.one.url_approve_reg,
        )

        text_correct = self.get_text(
            by=By.TAG_NAME, locator=settings.tests.one.text_correct
        )
        assert settings.tests.one.text_expected in text_correct
