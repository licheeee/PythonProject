
# -*- coding: UTF-8 -*-
# 计算一个整数的平方根，打印2位精度

import math

a = int(input("Please input a :"))

b = math.sqrt(a)

print("sqrt(a) = %.2f" % b)

# string.format
print ("sqrt(a) = {0:.2f}".format(b))