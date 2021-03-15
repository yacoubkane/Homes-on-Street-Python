from turtle import Turtle, Screen

def housesquare(turtle, width):
    for _ in range(4):
        turtle.forward(width)
        turtle.left(90)

def housetriangle(turtle, base):
    for _ in range(3):
        turtle.forward(base)
        turtle.left(120)

def housedoor(turtle, height, width):
    turtle.fillcolor('white')
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    

def house(turtle, hs, xroof, xdoor, xwindow, ywindow):
    turtle.fillcolor('cyan')
    turtle.begin_fill()
    housesquare(turtle, hs)
    turtle.penup()
    turtle.left(90)
    turtle.forward(hs)
    turtle.right(90)
    turtle.end_fill()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.forward(hs * xroof)
    turtle.pendown()
    housetriangle(turtle, hs)
    turtle.penup()
    turtle.right(90)
    turtle.forward(hs)
    turtle.left(90)
    turtle.end_fill()
    turtle.forward(hs * xdoor)
    turtle.pendown()
    housedoor(turtle, hs * 0.7, hs * 0.3)
    turtle.penup()
    turtle.backward(hs * xdoor)
    turtle.forward(hs * xwindow)
    turtle.left(90)
    turtle.forward(hs * ywindow)
    turtle.right(90)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()
    housesquare(turtle, hs * 0.1) #window 1
    turtle.penup()
    turtle.backward(hs * xwindow)
    turtle.pendown()
    turtle.end_fill()
    turtle.fillcolor('white')
    turtle.begin_fill()
    housesquare(turtle, hs * 0.1) #window 2
    turtle.penup()
    turtle.left(90)
    turtle.backward(hs * ywindow)
    turtle.right(90)
    turtle.pendown()
    turtle.end_fill()
    

screen = Screen()
kevin = Turtle()
kevin.speed(1000000000)
size = 250
kevin.penup()
kevin.goto(-900, 50)
kevin.pendown()

for factor in range(1, 29):
    house(kevin, size / factor, 0.0, 0.2, 0.6, 0.4)
    kevin.penup()
    kevin.forward(1 * size / factor)
    kevin.pendown()
