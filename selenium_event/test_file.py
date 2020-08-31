from selenium_event.base import Base
from  time import sleep

class TestFile(Base):
    #文件上传
    def test_file(self):
        self.driver.get('http://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id('stfile').send_keys('/Users/galaxy/Documents/HogwartsCode/image/logo100.png')
        sleep(3)