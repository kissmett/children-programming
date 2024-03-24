

for h in range(9):
    for t in range(9):
        for o in range(9):
            # a = h*100 + t*10 +o
            # if h**3+t**3+o**3 == a:
                # print(a)
            h1=h**3
            t1=t**3
            o1=o**3
            h2=h*100
            t2=t*10
            if h1+t1+o1==h2+t2+o:                
                print(h2+t2+o)

for i in range(999):
    # 将i的百位十位个位求出来
    h = i // 100
    t = (i - h*100) // 10 
    o = (i - h*100 - t*10)
    if h**3+t**3+o**3 == i:
        print(i)
e



