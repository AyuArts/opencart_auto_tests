from config import settings
from core.page import BasePage


class PageMain(BasePage):

    def open_page(self):
        self._driver.get(settings.default.url)
