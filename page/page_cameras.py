from page.page_products import PageProducts
from locators import BaseLocators as BL
from page.routers import routers as r


class PageCameras(PageProducts):

    def open_page(self):
        self._click_and_wait_for_url(BL.CAMERAS_LINK, r.CAMERAS_URL)
