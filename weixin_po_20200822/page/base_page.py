
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    _baseurl = ''
    def __init__(self,driver:WebDriver=None):
        self._driver = ''
        if driver is None:
            # 复用浏览器 在终端打
            # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
            option = Options()
            option.debugger_address = 'localhost:9222'
            self._driver = webdriver.Chrome(options=option)
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
        else:
            self._driver:WebDriver = driver

        if self._baseurl != '':
            self._driver.get(self._baseurl)

    def find(self,by,locator):
        return self._driver.find_element(by,locator)

    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)

    def base_quit(self):
        return self._driver.quit()
