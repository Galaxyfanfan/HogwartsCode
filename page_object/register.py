from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID,'corp_name').send_keys('hello')
        self.find(By.ID,'manager_name').send_keys('123')
        return True