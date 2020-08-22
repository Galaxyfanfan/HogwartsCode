#多窗口和frame

from  time import sleep

from selenium_event.base import Base


class TestWindows(Base):
    def test_windows(self):
        self.driver.get('https://www.baidu.com')
        login = self.driver.find_element_by_link_text('登录').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.switch_to.default_content()
        sleep(10)#解决加载慢 会提示'Message: Unable to locate element' 找不到元素
        zhuce = self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('123')
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()




