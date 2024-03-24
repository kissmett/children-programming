###########################################
#集合 [] {} ()
# [] 列表/数组


print('---------------------------------')

import random


# a = []
# for i in range(100):
#     a.append(random.randint(0,100))
# print(a)     
# a.sort()    
# print(a)    

#创建列表
a = [1,2,3,4,5]
print('a',a)
#向列表尾部添加一个元素
a.append(6)
print('a',a)
#获取列表中某一个位置的元素
print('a的第1个元素',a[0])
print('a的第2个元素',a[1])
print('a的第3个元素',a[2])
print('a的第4个元素',a[3])
print('列表a的长度',len(a))

#向列表中的一个位置插入一个元素
a.insert(3,3.5)
print('a',a)

a.insert(5,4.5)
print('a',a)
#遍历列表
sum = 0
for i in a:
    # sum = sum + i
    sum += i
    print(i)

max = a[0]
for e in a:
    if e>max:
        max=e
print(max)        

import pygame





print('---------------------------------')

