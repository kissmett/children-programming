import random
c=1
a=random.randint(1,100)
print(a)
list=[]
重复次数=int(input('请输入重复的次数：'))

# while True:
#     b=input('请输入b的内容：')
#     list.append(b)
#     if not c == 重复次数 :
#         c=c+1
#     else:
#         break        

while c <= 重复次数:
    b=input('请输入b的内容：')
    list.append(b)
    c = c + 1

print(list)        


#rty