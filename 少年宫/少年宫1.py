import turtle as t

#在（x,y)处画一个color色的正方形,并写出text                                                     
def drawRactangle(x,y,color,text):
    t.color(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(120)
        t.left(90)    
    t.end_fill()
    t.pencolor("white")
    t.write(text,align="left",font=("华文新魏",45,"normal"))

t.color("gold")
t.penup()
t.goto(0,0)
t.pendown()
t.write("新\n年\n快\n乐\n",align="left",font=("华文新魏",45,"normal"))
t.color("yellow")
t.penup()
t.goto(5,5)
t.pendown()
t.write("新\n年\n快\n乐\n",align="left",font=("华文新魏",45,"normal"))

drawRactangle(-125,-55,"red","中国\n飞人")
drawRactangle(-350,-55,"red","新年\n快乐")
drawRactangle(-350,-300,"gold","人间\n理想")
drawRactangle(-125,-300,"yellow","阖家\n幸福")
drawRactangle(300,-300,"red","年年\n有余")

t.done()
