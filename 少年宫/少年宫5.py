import turtle as t
def drawstar(x,y,size):
    #画五角星★
    #角度144
    t.color("yellow","yellow")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()    

#画长方形
t.penup()
t.goto(-300,200)
t.pendown()
t.color("red","red")
t.begin_fill()
for i in range(2):
    t.forward(600)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()
drawstar(-120,160,50)
drawstar(-80,120,50)
drawstar(-80,60,50)
drawstar(-120,20,50)
drawstar(-260,120,100)
t.done() 
