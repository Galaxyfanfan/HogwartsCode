from weixin_po_20200822.page.home import Home


class Test_Home():
    def setup(self):
        self.home = Home()

    def teardowm(self):
        self.home.base_quit()

    def test_contact(self):
        self.home.goto_contact().goto_add_contact()

    def test_add_member(self):
        self.home.goto_add_member().add_member()

    def test_add_contact(self):
        self.home.goto_add_contact().upload_file()