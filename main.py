import random
from turtle import Turtle, Screen


screen=Screen()
screen.setup(width=500, height=400)
is_race_on=False
user_bet=screen.textinput(title='Make your bet', prompt="Which turtle will win the race?Enter a "
                                                        "color")
colors=["red","orange","yellow","green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]
all_turtle=[]


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on=True

while is_race_on:
    for turtles in all_turtle:
        if turtles.xcor() >250:
            is_race_on=False
            winning_color=turtles.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} is the winner")
            else:
                print(f"You've lost! The {winning_color} is the winner")
        random_distance=random.randint(0,10)
        turtles.forward(random_distance)
screen.exitonclick()