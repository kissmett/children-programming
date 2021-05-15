import numpy as np
import random

all = np.arange(31)
# print(all)
left = all
exclude = []
show = []

#从未知归属的集合(left)中,选出n个数;
def geneRandomList(n):
    m = n
    if m >= left.size:
        m = int(left.size/2)
    res = []
    while len(res) < m:
        rn = random.randint(0,left.size-1)
        # print(unknown[rn])
        if left[rn] not in res:
            res.append(left[rn])
    #补全n个
    while len(res) < n:
        rn = random.randint(0,all.size-1)
        # print(unknown[rn])
        if all[rn] not in res:
            res.append(all[rn])
    return np.array(res)

#当只剩下一个元素时,输出所猜数字
print('从0-30中任意挑选一个数字,记在心里.')
while left.size != 1: 
    show = geneRandomList(10)
    print('它在这里吗?: ',show)

    answer = input('y/n ?')
    #如果不在,则排除本集合
    if answer == 'n':
        left = np.setdiff1d(left,show)
    
    #如果选择在备选集合中,则排除其他元素
    if answer == 'y':
        left = np.setdiff1d( left,np.setdiff1d(all,show) )
    
    if answer =='q':
        exit
    # print('left ', left, left.size)

print('你心里的数字是:',left[0])
#print(geneRandomList(3))
# print(random_int_list(1,31,10))