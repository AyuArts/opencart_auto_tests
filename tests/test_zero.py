from core.base_test import BaseTest
from config import settings
from selenium.webdriver.common.by import By


class TestZero(BaseTest):
    def test_brands(self):
        # STEP 1 open default url
        self.open_page()

        # STEP 2 Click on 'Brands' at the bottom of the page
        self.click_and_wait_for_url(
            By.LINK_TEXT,
            "Brands",
            url_contains=settings.tests.zero.url_contains,
        )

        # STEP 3 get elements by css selector
        brand_names = self.get_elements(
            By.CSS_SELECTOR,
            locator=settings.tests.zero.css_selector,
        )

        # STEP 4 check brands [Apple,Canon,Hewlett-Packard,HTC,Palm,Sony]
        for brand in settings.tests.zero.expected_brands:
            assert brand in brand_names, f"Brand '{brand}' not found on the page"
