from weixin_po_20200822.page.add_member import AddMember
from weixin_po_20200822.page.home import Home


class Test_Add_Member():
    def setup(self):
        self.home = Home()

    def test_add_member(self):
        #       1. 跳转到添加成员 2. 添加成员
        data = {
            'username' : 'hiii',
            'engname': 'hi',
            'acctid': '1233321',
            'phone': '13788880000',
        }
        result = self.home.goto_add_member().add_member(data)
        # assert "皮城女警" in result

    def test_add_member_fail(self):
        data = {
            'username' : 'hiii',
            'engname': 'hi',
            'acctid': '1233321',
            'phone': '13788880000',
        }
        self.home.goto_add_member().add_member(data)
        # result = AddMenber(self.home.driver).get_phone_error_message()
        # assert "请填写正确的手机号码" == result

    def test_contact_add_member(self):
        self.home.goto_add_contact().upload_file()

    def teardown(self):
        self.home.base_quit()

