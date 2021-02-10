"""
HogwartsCode - 当前Project名称;
TongLao - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2021/2/10 5:39 下午 
"""
# 定义一个天山童姥类 ，类名为TongLao
class TongLao:
    # 血量，武力值
    my_hp = ''
    my_power = ''

    def __init__(self,my_hp,my_power):
        self.my_hp = my_hp
        self.my_power = my_power

    def see_people(self,name):
        if name == 'WYZ' or name == '无崖子':
            print("师弟！！！！")
        elif name == '李秋水':
            print("呸，贱人")
        elif name == '丁春秋':
            print("叛徒！我杀了你")

    def fight_zms(self,your_hp,your_power):
        self.my_power = self.my_power * 10
        self.my_hp = self.my_hp / 2.0

        your_hp = your_hp - self.my_power
        self.my_hp = self.my_hp - your_power
        print('当前我的血量：',self.my_hp,'你的血量：',your_hp)

        if self.my_hp < your_hp:
            print('你赢了')
        elif your_hp < self.my_hp:
            print('我赢了')
        elif your_hp == self.my_hp:
            print('平局')


tonglao = TongLao(1000,100)
tonglao.see_people('李秋水')
tonglao.fight_zms(800,200)