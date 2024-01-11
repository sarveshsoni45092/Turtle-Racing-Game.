from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

bet_is_on = False
colors= ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
if user_bet:
    bet_is_on = True
    
while bet_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            bet_is_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"you won the Game !!, The {wining_color} Turtle is the Winner. !!")
            else:
                print(f"you lost the game. The {wining_color} Turtle is the Winner. !!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()