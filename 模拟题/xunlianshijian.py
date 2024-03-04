a,b,c,d = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

#全部转化为分钟 a小时b分钟 a*60 + b，
L = (c*60+d)-(a*60+b) #minute
# 将L转化为x小时y分钟
x = int(L/60)
y = L % 60
print(x,y)
