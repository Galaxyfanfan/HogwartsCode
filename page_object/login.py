from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from page_object.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR,'login_registerBar_link').click()
        return Register(self._driver)