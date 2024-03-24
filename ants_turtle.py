import turtle as t
import random

def cords():
    t.penup()
    for i in list(range(-16,16)):
        t.goto((i*20,-240))
        t.pendown()
        t.goto((i*20,240))
        t.penup()
    for i in list(range(-12,12)):
        t.goto((-320,i*20))
        t.pendown()
        t.goto((320,i*20))
        t.penup()


def ant():
    t.pencolor=t.color(random.choice(['red','orange','yellow','green','blue','purple','pink','black']))
    t.penup()
    t.goto(0,0)
    t.pendown()
    for i in list(range(50)):
        r = random.choice([0,90,-90,180])
        t.right(r)
        t.forward(20)
    t.penup()


t.delay(0)    
# cords()
for i in list(range(100)):
    ant()



t.mainloop()