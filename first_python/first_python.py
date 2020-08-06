
# 一个多回合制游戏，每个角色都有hp 和power，
# hp代表血量，power代表攻击力，hp的初始值为1000，
# power的初始值为200。打斗多个回合
# 定义一个fight方法：
# my_hp = hp - enemy_power
# enemy_final_hp = enemy_hp - my_power
# 谁的hp先为0，那么谁就输了
#每行需要加注释

#导入 随机数 系统库
import random

#方法
def fight():
    #我的血量 初始值1000
    my_hp = 1000
    #你的血量，初始值1000
    your_hp = 1000
    #我的攻击力。初始值200
    my_power = 200
    #你的攻击力，初始值200
    your_power = 200

    #循环 模拟回合
    while True:
        #获取一个只有1和2的随机数，1表示我打你一下，2表示你打我一下
        count = random.randint(1,2)
        if count == 1:
            #我赢了，打对方一下
            your_hp = your_hp - my_power
        else:
            #你赢了，打我一下
            my_hp = my_hp - your_power

        #打印 每次回合后各自的血量
        print('当前我的血量：',my_hp,'你的血量：',your_hp)

        #当我的血量小于0时，你赢了
        if my_hp <= 0:
            print('你赢了')
            #退出循环
            break
        #当你的血量小于0时，我赢了
        if your_hp <= 0:
            print('我赢了')
            #退出循环
            break

#调用方法，游戏开始
fight()