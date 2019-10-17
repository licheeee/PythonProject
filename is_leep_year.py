# -*- coding: UTF-8 -*-
# 判断一个年份是否是闰年

year = int(input("Plear input a year:"))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leep year".format(year))
        else:
            print("{0} is not a leep year".format(year))
    else:
        print("{0} is a leep year".format(year))
else:
    print("{0} is not a leep year".format(year))

