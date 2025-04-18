import pytest
from core.base_test import BaseTest
from config import settings
from selenium.webdriver.common.by import By


class TestTwo(BaseTest):
    def test_two(self):
        self.open_page()

        self.cursor_guidance(
            By.LINK_TEXT,
            settings.tests.two.dropdown,
        )

        self.click(
            By.LINK_TEXT,
            settings.tests.two.button_text,
        )
        assert (
            self.first_selected(By.ID, settings.tests.two.input_limit_id).text
            == settings.tests.two.input_limit_value_def
        )
        assert (
            self.first_selected(By.ID, settings.tests.two.input_sort_id).text
            == settings.tests.two.input_sort_value_def
        )
        assert (
            len(self.find_elements(By.CLASS_NAME, settings.tests.two.product_layout))
            == settings.tests.two.product_count
        )

        self.select_by_visible_text(
            By.ID,
            settings.tests.two.input_limit_id,
            settings.tests.two.input_limit_value_new,
        )
        assert (
            self.first_selected(By.ID, settings.tests.two.input_limit_id).text
            == settings.tests.two.input_limit_value_new
        )

        pagination = self.find_element(
            By.CSS_SELECTOR, settings.tests.two.pagination_selector
        )
        assert pagination.text == settings.tests.two.pagination_text

        self.execute_script(settings.tests.two.script_scroll)
        assert pagination.is_displayed()
