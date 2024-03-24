'''
1~59 不及格
60~84合格
85~100 优秀
'''

score = int(input("please input your score(integer):"))

中文变量 = score #python可以用中文命名变量
print(中文变量)
if score > 100:
    print("input error! too big")
elif score<= 100 and score >=85:
        print("excellent")
elif score <=85 and score >=60:
    print("ok")
elif score <=59 and score >=0:
    print("not ok")
else:
    print("input error! too small, GET OUT!!!")
    print("你上学怎么上的？？？！！！")                
