from core.page import BasePage
from locators import BrandLocators as PL  # PL - page locators
from locators import BaseLocators as BL  # BL - base locators
from page.routers import routers as r


class PageBrands(BasePage):
    def open_page(self):
        self._click_and_wait_for_url(BL.BRANDS_LINK, r.BRANDS_URL)

    def get_brands(self):
        return self._get_elements_text(PL.BRANDS_ELEMENTS)
