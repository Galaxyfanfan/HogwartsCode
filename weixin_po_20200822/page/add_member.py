from selenium.webdriver.common.by import By

from weixin_po_20200822.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self,data):
        self.find(By.ID,'username').send_keys(data['username'])
        self.find(By.ID, 'memberAdd_english_name').send_keys(data['engname'])
        self.find(By.ID, 'memberAdd_acctid').send_keys(data['acctid'])
        # self.find(By.XPATH, '//*[@class="ww_label ww_label_Middle"] and /[@span="女"]').click()
        self.find(By.ID, 'memberAdd_phone').send_keys(data['phone'])
        # self.find(By.XPATH,'//*[@class="qui_btn ww_btn ww_btn_Blue js_btn_continue"]').click()
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()

