# coding : utf-8

#实现一个简单条件控制
#猜数字

Num = 7
YourNum = 0

print ('猜数字游戏')
while YourNum != Num :
    YourNum = int(input('请输入你的数字'))
    if YourNum > Num :
        print ('你猜的数字大了')
    elif YourNum < Num :
        print ('你猜的数字小了')
    else :
        print ('你猜对啦')

input ('输入任意键退出程序')
