from page.page_products import PageProducts
from locators import BaseLocators as BL
from page.routers import routers as r


class PageShowAll(PageProducts):
    def open_page(self):
        self._cursor_guidance(BL.DESKTOPS_LINK)
        self._click_and_wait_for_url(BL.SHOW_ALL_LINK, r.SHOW_ALL_URL)
