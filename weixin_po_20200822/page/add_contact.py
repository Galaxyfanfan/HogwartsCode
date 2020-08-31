from selenium.webdriver.common.by import By

from weixin_po_20200822.page.base_page import BasePage


class AddContact(BasePage):
    def upload_file(self):
        pass
        #这里有问题
        # self.find(By.ID,'js_upload_file_input').click()

        # self.find(By.XPATH,'//*[@id="file_select_form"]//label').click()