
from selenium import webdriver
from selenium.webdriver import TouchActions
from  time import sleep

class TestTouchAction():
    def setup(self):
        #报错解决
        #Cannot call non W3C standard command while in W3C mode
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver  = webdriver.Chrome(chrome_options=opt)
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_scrollbottom(self):
        self.driver.get('https://www.baidu.com')
        ele = self.driver.find_element_by_id('kw')
        ele.send_keys('python')

        search = self.driver.find_element_by_id('su')

        action = TouchActions(self.driver)
        # action.tap(ele)
        action.tap(search)
        action.perform()

        #滑动
        action.scroll_from_element(ele,0,10000)
        action.perform()