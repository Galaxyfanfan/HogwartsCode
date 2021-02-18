
from typing import List
import pytest


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 修改编码
    # 将 编码格式unicode转化为中文
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


    # 可以放fixture方法
    # @pytest.fixture(scope='module')#作用域（session>module>class>function）
    # def login():
    #     print('登录')
    #     yield 'name'
    #     print('登出')

#顶头写
@pytest.fixture(scope='module',autouse=True)
def dayin():
    print('fixture-开始计算')
    yield
    print('fixture-结束计算')
