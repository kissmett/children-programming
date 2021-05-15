n1 = 0
n2 = 1
n3 = 0
for i in range(200):
    n3 = n2 + n1
    print('%s:%s'%(i+1,n3))
    n1 = n2
    n2 = n3