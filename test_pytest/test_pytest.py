
"""
pytest 命名规则
文件名：以 test_开头 （test_*.py）
类名：以 Test 开头
方法名：以test_开头
"""

import pytest
import yaml
from Calculator.Calculator import Calculator

def setup_module(self):
    print('模块级别：setup_module 开始')

def teardown_module(self):
    print('模块级别：teardown_module 结束')

def setup_function(self):
    print('函数级别：setup_function 开始')

def teardown_function(self):
    print('函数级别：teardown_function 结束')

def test_func():
    print('test 函数')


def getdatas():
    # 获取yaml数据
    with open('./datas/calc.yml', encoding='utf-8') as file:
        datas = yaml.safe_load(file)
        print('--------------datas------------')
        add = datas['add']
        sub = datas['sub']
        div = datas['div']
        mul = datas['mul']
        myids = datas['myids']

    return [add,sub,div,mul,myids]

class TestCalculator:
    def setup_class(self):
        # 实例化
        self.calc = Calculator()
        print('类级别：setup_class 开始')

    def teardown_class(self):
        print('类级别：teardown_class 结束')

    def setup(self):
        print('开始计算')

    def teardown(self):
        print('计算结束')

    # 参数化
    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',getdatas()[0],ids=getdatas()[4])
    # 加法
    def test_add(self,a,b,expect):
        # python机制的问题，0.1+0.2=0.30000000000000004
        # 所以做保留两位小数处理
        result = round(self.calc.add(a,b),2)
        assert expect == result

    # 减法
    @pytest.mark.parametrize('a,b,expect', getdatas()[1])
    def test_sub(self,a,b,expect):
        result = round(self.calc.sub(a,b),2)
        assert expect == result

    # 除法
    @pytest.mark.parametrize('a,b,expect', getdatas()[2])
    def test_div(self,a,b,expect):
        result = round(self.calc.div(a,b),2)
        assert expect == result

    # 乘法
    @pytest.mark.parametrize('a,b,expect', getdatas()[3])
    def test_mul(self,a,b,expect):
        result = round(self.calc.mul(a,b),2)
        assert expect == result






#
# if __name__ == '__main__':
#     pytest.main(['test_pytest.py'])
#      pytest test_pytest.py -v
#
#     pytest.main(['test_pytest.py::TestDemo','-v'])
#     python test_pytest.py


