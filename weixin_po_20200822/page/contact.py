from time import sleep

from selenium.webdriver.common.by import By

from weixin_po_20200822.page.base_page import BasePage
from weixin_po_20200822.page.add_member import AddMember
from weixin_po_20200822.page.add_department import AddDepartment
class Contact(BasePage):
    _baseurl = 'https://work.weixin.qq.com/wework_admin/frame#contacts'

    def goto_add_contact(self):
        pass

    def goto_add_member(self):
        self.find(By.XPATH, '//*[@id="js_contacts106"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        return AddMember(self._driver)

    def goto_add_department(self):
        self.find(By.XPATH,'//*[@class="member_colLeft_top_addBtn"]').click()
        self.find(By.XPATH,'//*[@class="js_create_party"]').click()
        return AddDepartment(self._driver)

    def get_department_list(self):
        self._driver.refresh()
        sleep(2)#这里不是很明白，如果不做刷新和延时 页面获取不到新加入的部门
        elements = self.finds(By.XPATH,'//*[@class="member_colLeft_bottom"]//*[@class="jstree-anchor"]')
        elements_text = []
        for ele in elements:
            elements_text.append(ele.text)

        return elements_text