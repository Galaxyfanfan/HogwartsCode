"""
HogwartsCode - 当前Project名称;
XuZhu - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2021/2/10 5:57 下午 
"""
from second_python.work2.TongLao import TongLao


class XuZhu(TongLao):

    def read(self):
        print('罪过罪过')


xuzhu = XuZhu(1000,300)
xuzhu.read()
