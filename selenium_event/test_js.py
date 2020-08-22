
from  time import sleep
import pytest
from selenium_event.base import Base


class TestJS(Base):

    @pytest.mark.skip
    def test_js(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('ios')
        #获取id
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        sleep(3)
        #滑动
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(5)

        # for code in [ 'return document.title' , 'return JSON.stringify(performance.timing)']:
        #     print('code' + code)
        #     print(self.driver.execute_script(code))

        print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))

#这里无法修改参数 不知道是什么原因
    def test_date(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script('document.getElementById("train_date").value="2021-12-01"')
        sleep(3)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
