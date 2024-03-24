def change(a,b):
        print('---------in function begin-------------')
        print(a,b)
        a,b=b,a
        print(a,b)
        print('---------in function end-------------')
        

x = 8
y = 1111
change(x,y)
print('x:',x)
print('y:',y)

x,y = y,x
print('x:',x)
print('y:',y)


