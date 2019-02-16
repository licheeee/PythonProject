# coding : utf-8

# python 迭代器
# 可以记住遍历位置的对象，只能向前不能后退
# 基本方法是iter()和next()

import sys


class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if (self.num < 3):
            value = self.num
            self.num = self.num + 1
            return value
        else:
            raise StopIteration


myNumbers = MyNumbers()
myIt = iter(myNumbers)


while True:
   try:
       print (next(myIt))
   except StopIteration:
       sys.exit()


list = [1, 2, 3, 4]

it = iter(list)

#for i in it :
#    print (i, end = ' ')


while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()

