import turtle
x = int(input("Długość boku: "))
a = turtle.Turtle()
i = 0
a.speed(100)
for i in range(4):
    a.fd(x)
    a.right(90)
    i=i+1
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos(x/4,0)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos((x/4)*2,0)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos((x/4)*3,0)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos(0,-(x/4))
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos(x/4,-(x/4))
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos((x/4)*2,-(x/4))
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos((x/4)*3,-(x/4))
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos(0,(-(x/4))*2)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos(x/4,(-(x/4))*2)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos((x/4)*2,(-(x/4))*2)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos((x/4)*3,(-(x/4))*2)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos(0,(-(x/4))*3)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos(x/4,(-(x/4))*3)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos((x/4)*2,(-(x/4))*3)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1
a.penup()
a.setpos((x/4)*3,(-(x/4))*3)
a.pendown()
for i in range(4):
    a.fd(x/4)
    a.right(90)
    i=i+1