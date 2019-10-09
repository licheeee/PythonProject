# -*- coding: UTF-8 -*-
# 计算二次方程的解

# a*x**2+b*x+c=0
# delta = b**2-4*a*c
# x1 = (-b+sqrt(delta))/(2*a)
# x2 = (-b-sqrt(delta))/(2*a)

import math

a, b, c = map(int, input("Please input a, b, c:").split())

delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print ("The answer is x1 = {0:.2f}, x2 = {1:.2f}".format(x1, x2))