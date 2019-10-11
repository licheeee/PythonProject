# -*- coding: UTF-8 -*-
# 计算圆面积

def roundArea(r):
    PI = 3.14
    return PI * r * r
    

r = int(input("Please input radius of circular surface : "))
area = roundArea(r)
print("The round area is {0:.2f}".format(area))
