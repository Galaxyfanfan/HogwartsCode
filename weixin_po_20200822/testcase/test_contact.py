from weixin_po_20200822.page.contact import Contact


class TestContact():
    def setup(self):
        self.contact = Contact()

    def teardowm(self):
        self.contact.base_quit()



    def test_add_department(self):
        name = '听见8'
        elements_text = self.contact.goto_add_department().add_department(name).get_department_list()
        assert name in elements_text
