'''
    随机生成1-100间的数字，进行猜一猜的功能

'''
#导入random模块
import random

#随机生成1-100之间的数字
randomNumber = random.randint(1,100)
# print(randomNumber)


while True:
    #用户输入的数字
    inputNumber = int(input("请输入您猜测的数字："))
    print(inputNumber)
    # cin >> inputNumber;
    # cout << inputNumber;
    print(type(randomNumber),type(inputNumber))
    print(randomNumber == inputNumber )

    #------------------------
    if  inputNumber < randomNumber:
        print("小了")
    elif inputNumber > randomNumber:
        print("大了")
    else:
        print("猜对了")
        break

answer = input("好玩吗？")
if answer == "yes":
    print("thanks")
else:
    print('下次改正')
