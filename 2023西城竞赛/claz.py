n = input()
n = int(n)
i = 0
while n != 1:
    i += 1
    if n % 2 == 0:
        n = n / 2
    else:
        n = (3 * n) + 1
print(i)