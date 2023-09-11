#数据类型
#整型integer int/浮点型float/字符型string str/布尔型boolean bool
from grpc import ssl_server_certificate_configuration


a1 = 3
a2 = 2
b1 = -1.5
b2 = 1.2e9
c = 'jesson'
d1 = True
d2 = False

print('---------------------------------')
print('a1=',a1,' a2=',a2)
print('b1=',b1,' b2=',b2,' c=',c)
print('d1=',d1,' d2=',d2)
print('type(a1)',type(a1))
print('type(b2)',type(b2))
print('type(c)',type(c))
print('type(d1)',type(d1))

a3 = a1
print('type(a3)',type(a3))

a3 = float(a1)
print('type(a3)',type(a3))

a3 = str(a1)
print('type(a3)',type(a3))

a3 = int(b1)
print('type(a3)',type(a3))
print('a3=',a3)

a3 = str(b2)
print('type(a3)',type(a3))
print('a3=',a3)


#运算符
#四则运算 + - * / **
print('a1/a2=',a1/a2) #python2 此处结果为1,为什么?

#逻辑运算符
# > == < >= <= != and or
print('a1>=a2 ',a1>=a2)
print('d1 and d2 ', d1 and d2)
print('d1 or d2 ', d1 or d2)

if d1 and d2:
    print("d1 and d2 条件成立")
else:
    print('d1 and d2 条件不成立')

if d1 or d2:
    print("d1 or d2 条件成立")
else:
    print('d1 or d2 条件不成立')
'''
if  xxx:
    ss
elif xxxx:

elif iiii:

else:
    sss
'''


###########################################
#集合 [] {} ()
# [] 列表/数组

print('---------------------------------')
