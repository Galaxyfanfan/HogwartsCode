from selenium.webdriver.common.by import By

from weixin_po_20200822.page.add_contact import AddContact
from weixin_po_20200822.page.add_member import AddMember
from weixin_po_20200822.page.base_page import BasePage
from weixin_po_20200822.page.contact import Contact


class Home(BasePage):
    _baseurl = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_contact(self):
        self.find(By.ID, 'menu_contacts').click()
        return Contact(self._driver)

    def goto_add_member(self):
        self.find(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        return AddMember(self._driver)

    def goto_add_contact(self):
        self.find(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]').click()
        return AddContact(self._driver)