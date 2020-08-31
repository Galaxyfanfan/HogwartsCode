import shelve

import pytest

from weixin_po_20200822.page.main import Main


class Test_Main():
    def setup(self):
        self.main = Main()

    def test_login(self):
        self.main.goto_login().login()

    @pytest.mark.skip
    def test_register(self):
        self.main.goto_register().register()

    def teardowm(self):
        self.main.base_quit()