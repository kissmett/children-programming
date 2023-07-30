for i in range(1,10):
    # for j in range(1,i+1):
    for j in range(1,10):
        print("{: <13}".format(" %s x %s = %s  " % (j,i,i*j)),end='')
    print('')
    # print(i)