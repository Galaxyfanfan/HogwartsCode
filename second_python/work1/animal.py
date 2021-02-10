"""
HogwartsCode - 当前Project名称;
animal - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2021/2/10 5:04 下午 
"""
# 动物 父类
class Animal:
    name = ''
    color = ''
    leg_num = ''

    def __init__(self,**kargs):
        self.name = kargs["name"]
        self.color = kargs["color"]
        self.leg_num = kargs["leg_num"]

    def run(self):
        print(f"{self.name}在用{self.leg_num}条腿奔跑")

    def walk(self):
        print(f"{self.name}在用{self.leg_num}条腿走路")

    def eat(self,food):
        print(f"{self.name}在吃{food}")

# 实例化一个子类
pig = Animal(name = '猪',color = 'pink', leg_num = 4)
pig.run()
print(f'{pig.name}的颜色是{pig.color}')
pig.eat('苹果')

# 实例化一个子类
penguin = Animal(name = '企鹅', leg_num = 2,color = '黑白相间')
penguin.walk()
print(f'{penguin.name}的颜色是{penguin.color}')
penguin.eat('鱼')
