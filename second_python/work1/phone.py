"""
HogwartsCode - 当前Project名称;
phone - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2021/2/10 5:27 下午 
"""

class Phone:
    phone_name = ''
    screen_width = 0
    screen_heght = 0
    color = ''


    def __init__(self,*args):
        self.phone_name = args[0]
        self.screen_width = args[1]
        self.screen_heght = args[2]
        self.color = args[3]


    def call(self,phone_num):
        print(f"{self.phone_name}给{phone_num}打电话")

    def send_message(self):
        print("发短信")

    def get_phone_size(self):
        return self.screen_width,self.screen_heght


apple = Phone('苹果',100,200,'red')
apple.call('123')
apple_size = apple.get_phone_size()
print(f'{apple.phone_name}的屏幕尺寸为{apple_size}')

xiaomi = Phone('小米',110,220,'blue')
xiaomi.send_message()
xiaomi_size = xiaomi.get_phone_size()
print(f'{xiaomi.phone_name}的屏幕尺寸为{xiaomi_size}')