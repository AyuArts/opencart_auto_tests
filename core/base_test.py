
from core.web_driver import driver as dr



class BaseTest:
    def setup_method(self):
        self.driver = dr
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

