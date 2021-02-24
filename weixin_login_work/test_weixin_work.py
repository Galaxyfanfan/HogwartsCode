import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

class TestWeiXin():
    def setup(self):
        #复用浏览器 在终端打
        #/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

        # option = Options()
        # option.debugger_address = 'localhost:9222'
        # self.driver = webdriver.Chrome(options=option)

        self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_contacts(self):
        # self.save_cookie()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        cookies = self.get_cookie()
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        self.driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element_by_css_selector('.ww_fileImporter_fileContainer_uploadInputMask').send_keys('/Users/galaxy/Downloads/test.xlsx')
        name = self.driver.find_element_by_css_selector('.ww_fileImporter_fileContainer_fileNames').text
        assert 'test.xlsx' == name


    #利用Shelve数据库存取cookie
    def save_cookie(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        cookies = self.driver.get_cookies()
        # Shelve 小型的数据库， 对象持久化保存方法，
        db = shelve.open("logincookies.db")
        # 存储
        db['cookie'] = cookies
        print(cookies)
        db.close()

    def get_cookie(self):
        db = shelve.open("logincookies.db")
        # 读取
        cookies = db['cookie']
        db.close()
        return cookies

    def test_save_cookie(self):
        self.save_cookie()

