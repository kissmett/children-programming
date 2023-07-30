# python的数组（列表）array list;
a = [1,2,3,4,5]
print(a[0])

b = list(range(10))
print(b)
# for i in b:
#     print(i)
b.append(10)
print(b)
b.insert(3,'jesson')
b[3] = 'jesson and george'
b[4] = 'tianfei and zhengyan'
del b[0]
print(b)
print(len(b))