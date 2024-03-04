#判断一个数是否为奇数，若是返回True，若否返回False
def isOdd(n):
    if n % 2==1:
        return True
    else:
        return False
    pass

#判断一个数是否为偶数，若是返回True，若否返回False
def isEven(n):
    if n % 2==0:
        return True
    else:
        return False
    pass

#返回一个数的绝对值
def abs(n):
    if n >=0:
        return n
    else:
        return n*-1
    pass

print(isOdd(33)) #期待输出True
print(isOdd(44)) #期待输出True
print(isEven(33)) #期待输出True
print(isEven(56)) #期待输出True
print(abs(9)) #期待输出9
print(abs(-9)) #期待输出9