from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    _baseurl = ''
    def __init__(self,driver:WebDriver=None):#解决类型识别的问题
        self._driver = ''
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
            self._driver.maximize_window()
        else:
            self._driver = driver

        if self._baseurl != '':
            self._driver.get(self._baseurl)

    def find(self,by,locator):
        return self._driver.find_element(by,locator)