
import random

personTryList=[] #尝试次数

personTryDictionary = {}




while True:
    nickName = input("请输入昵称:")
    print('nikeName:',nickName)

    randomNumber = random.randint(1,100)
    print(randomNumber)

    inputNumber =  int(input("please guess a number between 1 and 100:"))

    perfect=10

    print('----------',personTryDictionary.keys())

    尝试次数=0
    if  nickName not in personTryDictionary.keys() :    
        personTryDictionary[nickName] = 尝试次数
        print('进行前打印personTryDictionay:',personTryDictionary)


    while not(inputNumber == randomNumber) :
        if inputNumber < 1:
            print("please input again. toooooo small.")
            尝试次数=尝试次数+1
            # exit()
        elif inputNumber > 100:
            print("please input again. toooooo large.")
            尝试次数=尝试次数+1
        elif inputNumber < randomNumber:
            print("小了")
            尝试次数=尝试次数+1
        elif inputNumber > randomNumber:
            print("大了")  
            尝试次数=尝试次数+1

        # elif inputNumber == randomNumber:
        #     print("对了")          
        inputNumber =  int(input("please guess a number between 1 and 100:"))
    print("对了")  

    personTryDictionary[nickName] = 尝试次数
    print('完成后打印personTryDictionay:',personTryDictionary)

# if 尝试次数<perfect:
#     perfect=尝试次数
    
