a = [2,4,3,9]
a = sorted(a)
print(a)
cnt = 0
for i in a:
    for j in a:
        for k in a:
            if i!=j and i!=k and j!=k:
                print(i,j,k)
                cnt = cnt + 1
            else:
                print(i,j,k,"--")
print('count: ',cnt)            