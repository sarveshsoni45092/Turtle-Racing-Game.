from turtle import Turtle,Screen

tim = Turtle()

screen = Screen()

def Go_forward():
    tim.forward(20)

def Go_back():
    tim.back(20)

def Go_clockwise():
    tim.right(15)

def Go_anticlockwise():
    tim.left(15)

def Click_clear():
    tim.clear()
    tim.penup()
    tim.goto(0,0)
    tim.pendown()
    tim.heading(90)

screen.listen()

screen.onkey(key="w",fun=Go_forward)
screen.onkey(key="s",fun=Go_back)
screen.onkey(key="d",fun=Go_clockwise)
screen.onkey(key="a",fun=Go_anticlockwise)
screen.onkey(key="c",fun=Click_clear)

screen.exitonclick()