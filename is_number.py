# -*- coding: UTF-8 -*-
# 判断字符串是否为数字

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    
    return False



print(is_number("1"))

print(is_number("1.1"))

print(is_number("a"))

