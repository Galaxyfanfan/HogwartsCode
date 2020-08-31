from selenium.webdriver.common.by import By

from weixin_po_20200822.page.base_page import BasePage
from weixin_po_20200822.page.login import Login
from weixin_po_20200822.page.register import Register


class Main(BasePage):
    _baseurl = 'https://work.weixin.qq.com/'

    def goto_register(self):
        self.find(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return Login(self._driver)
