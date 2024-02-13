def f (l):
    x1=1
    for x1 in range(1,l+1):
        
        for x2 in range(x1,l+1):
            a=x1*x2
            print('{0}*{1}={2}'.format(x1,x2,a),end=' ')
        print("\n")
for i in range(10):
    f(i)
    print('-----------------')
# x1=1
# for x1 in [1,2,3,4,5,6,7,8,9]:    
#     for x2 in range(1,10):
#         if x1 <= x2:
#             a=x1*x2
#             print('{0}*{1}={2}'.format(x1,x2,a),end=' ')
#     print("\n")
            