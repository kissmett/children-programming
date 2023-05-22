import turtle as t
t.setup(800,600,200,200)
#240，200     0，200
t.pensize(20)
t.penup()
t.goto(-240,200)
t.pendown()
t.color('blue','white')
t.circle(-100)



t.penup()
t.goto(0,200)
t.pendown()
t.color('black','white')
t.circle(-100)


t.penup()
t.goto(240,200)
t.pendown()
t.color('red','white')
t.circle(-100)



t.penup()
t.goto(-120,100)
t.pendown()
t.color('orange','white')
t.circle(-100)



t.penup()
t.goto(120,100)
t.pendown()
t.color('green','white')
t.circle(-100)
t.penup()
t.goto(-240,200)
t.pendown()



t.color('blue','white')
t.circle(-100,180)

t.penup()
t.goto(-120,100)
t.pendown()
t.color('orange','white')
t.circle(100,-277)


t.penup()
t.goto(0,200)
t.pendown()
t.color('black','white')
t.setheading(0)
t.circle(-100,200)




t.penup()
t.goto(120,100)
t.pendown()
t.color('green','white')
t.setheading(0)
t.circle(-100,277)



t.penup()
t.goto(240,200)
t.pendown()
t.color('red','white')
t.setheading(0)
t.circle(-100,200)

t.done()