import turtle as t

# a = 1
def a():
    print("ok")
a=[]
for i in range(10):
    a.append(t.pos())
    t.forward(i*3)
    t.left(55)
    t.write(t.pos(), move=False, align="left", font=("Arial", 4, "normal"))
a.append(t.pos())
print(a.__len__())
print(len(a))
print(a)