import selenium
from  selenium import  webdriver
from  time import  sleep
# def test_selenium():
#     # driver = webdriver.Chrome()
#     driver = webdriver.Firefox()
#     driver.get('http://www.baidu.com')

class TestHogwards():

    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)#动态等待5秒

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get('http://www.testerhome.com')
        self.driver.find_element_by_link_text('社团').click()
        self.driver.find_element_by_link_text('求职面试圈').click()
        # self.driver.find_element_by_link_text('.topic-22621 .title > a').click()
        self.driver.find_element_by_class_name('.topic-23386 .title > a').click()


