# -*- coding: UTF-8 -*-
# 判断一个数字是否是质数

num = int(input("Please input a number :"))

primeFlag = True
sqrt = int(num ** 0.5)
for i in range(2, sqrt + 1):
    if (num % i) == 0:
        print("{0} is not a prime number.".format(num))
        break
else:
    print("{0} is a prime number.".format(num))

