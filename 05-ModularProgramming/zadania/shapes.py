import turtle
def drawSquare():
    x = int(input("Podaj współrzędną x lewego górnego rogu kwadratu: "))
    y = int(input("Podaj współrzędną y lewego górnego rogu trójkata: "))
    n = int(input("Podaj długość boku kwadratu: "))
    pen = turtle.Turtle()
    i = 0
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    while i<4:
        pen.forward(n)
        pen.right(90)
        i=i+1
drawSquare()
