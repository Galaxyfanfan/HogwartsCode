#表单

from selenium import webdriver
from selenium.webdriver import TouchActions
from  time import sleep

class TestForm():
    def setup(self):
        self.driver  = webdriver.Chrome()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get('https://testerhome.com/account/sign_in')
        user_login = self.driver.find_element_by_id('user_login').send_keys('123')
        user_password = self.driver.find_element_by_id('user_password').send_keys('password')
        user_remember_me = self.driver.find_element_by_id('user_remember_me').click()
        login = self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        sleep(3)

