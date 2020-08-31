from page_object.main import Main


class TestRegister():
    def setup(self):
        self.main = Main()
    def tearDown(self):
        self.main._driver.quit()

    def test_register(self):
        # assert self.main.goto_register().register()
        assert self.main.goto_login().goto_register().register()