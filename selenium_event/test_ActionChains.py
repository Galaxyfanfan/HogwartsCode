import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestActionChains():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        click = self.driver.find_element_by_xpath("//input[@value='click me']")
        doubleClick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        rightClick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(click)
        action.double_click(doubleClick)
        action.context_click(rightClick)

        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_moveToElement(self):
        self.driver.get('https://www.baidu.com')
        # ele = self.driver.find_element_by_link_text("设置")
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        #拖拽
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        dragger = self.driver.find_element_by_id('dragger')
        droper = self.driver.find_element_by_xpath('/html/body/div[2]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(dragger,droper).perform()
        action.click_and_hold(dragger).release(droper).perform()
        sleep(3)

    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        action = ActionChains(self.driver)
        action.click(ele)
        action.send_keys('username').pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('nini').pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)
