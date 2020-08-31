from time import sleep

from selenium.webdriver.common.by import By

from weixin_po_20200822.page.base_page import BasePage



class AddDepartment(BasePage):
    def add_department(self,name):
        from weixin_po_20200822.page.contact import Contact

        self.find(By.XPATH,'//*[@class="qui_inputText ww_inputText"]').send_keys(name)
        self.find(By.CSS_SELECTOR,'.js_parent_party_name').click()
        self.find(By.XPATH,'//*[@id="__dialog__MNDialog__"]//*[@class="jstree-anchor"]').click()
        self.find(By.XPATH,"//*[@id='__dialog__MNDialog__']//*[@class='qui_btn ww_btn ww_btn_Blue']").click()

        return Contact(self._driver)