from page.page_product import PageProduct
from locators import BaseLocators as BL
from page.routers import routers as r


class PageIphone(PageProduct):

    def open_page(self):
        self._click_and_wait_for_url(BL.IPHONE_LINK, r.IPHONE_URL)
