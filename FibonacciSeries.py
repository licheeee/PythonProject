# coding : utf-8 

a, b = 0, 1
while b < 10 :
    print (b)
    a, b = b , a + b



# end=''可以输出到一行
a, b = 0, 1
while b < 10 :
    print (b, end=',')
    a, b = b , a + b