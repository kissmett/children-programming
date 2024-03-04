'''
求n的因数的个数
'''
n = input()
n = int(n)
n0 = n
i = 1
s = 0
ins = []
while (i<=n):
    if n % i == 0:
        print('--',n,i)
        n = int(n0/i)
        if(not i in ins) :
            ins.append(i)
        if(not n in ins) :
            ins.append(n)
        # if n == i:
        #     s += 1
        # else:
        #     s += 2            
        print(i,int(n0/i),n)
    i +=1
print(len(ins))