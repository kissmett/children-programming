import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
sides = 6
for x in range(1000):
    t.pencolor(colors[x%sides])
    t.forward(x)
    t.left(66)
turtle.mainloop()