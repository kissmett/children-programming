a=[1,1,2,1,3,4,1,2,2]

def getSingleValue(arr):
    newarr = []
    d = {}
    for i in arr:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] = d[i] + 1
    for k in d.keys():
        if d[k]==1:
            newarr.append(k)           
    return newarr
    
print('single:',getSingleValue(a))


def getuniq(arr):
    newarr=[]
    for i in range(len(arr)):
        if a[i] in newarr:
            newarr.remove(a[i])
        else:
            newarr.append(a[i])
    return newarr

print(getuniq(a))


def getuniq1(arr):
    newarr=[]
    for i in arr:
    # for i in range(len(arr)):
        if i  not in newarr:
            newarr.append(i)
    return newarr

print(getuniq1(a))