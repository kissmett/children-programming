import random

list = [4,5,'jesson','tf']
r1=random.choice(list)

r2 = random.randint(1,10)
print(type(r1),type(r2))

# random(),返回 0<= n <1之间的随机实数n
randomNumber1 = random.random()

# choice(seq) 从序列seq中返回随机的元素
list = ["张三"]
randomNumber2 = random.choice(list)

# randint() 随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值
randomNumber3 = random.randint(4,10)
print(type(randomNumber1),type(randomNumber2),type(randomNumber3))