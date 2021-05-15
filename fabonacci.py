n1 = 0
n2 = 1
i = 0
while (i < 100):
    n3 = (n1 + n2)
    n1 = n2
    n2 = n3
    print(n3)
    i += 1
print('--------')

def fib2(n):

    n1 = 0
    n2 = 1
    i = 0
    while (i < n):
        n3 = (n1 + n2)
        yield n3
        n1 = n2
        n2 = n3
        print('print: ', n3)
        i += 1

for i in fib2(100):
    print('yeild: ', i)

def fib(n):

    if (n == 1):
        return 1
    if (n == 0):
        return 0
    return (fib(n - 1) + fib(n - 2))

print(fib(10))
