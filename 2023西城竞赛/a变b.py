a,b = input().split()
a = int(a)
b = int(b)

i = 0
while a != b:
    i += 1
    if b % 2 == 0 and b / 2 >=a: 
        b = b / 2
    else:
        b = b - 1
print(i)        