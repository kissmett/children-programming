def collatz(n):
    while n != 1:
        print n  
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)

# 选择一个起始数字
starting_number = int(input("give me a number: "))
collatz(starting_number)
