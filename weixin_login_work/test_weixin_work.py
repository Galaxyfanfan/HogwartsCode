from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWeiXin():
    def setup(self):
        #复用浏览器 在终端打
        #/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        # cookies = self.driver.get_cookies()
        # print(cookies)

        cookies = []

        for cookie in cookies:
            print(cookie)
            if 'expiry' in cookie.keys():
                cookies.pop()
                self.driver.add_cookie(cookie)




    def test_login(self):
        pass