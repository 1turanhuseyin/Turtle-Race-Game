from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.setheading(320)
finish_line.forward(270)
finish_line.setheading(90)
finish_line.pendown()

def draw_dashed_line(length, dash_length=5):
    for i in range(length // dash_length):
        finish_line.speed(0)
        finish_line.forward(dash_length)
        finish_line.penup()
        finish_line.forward(dash_length)
        finish_line.pendown()

draw_dashed_line(180)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x_position = -230
y_position = -125

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.turtlesize(1.5)
    timColor = random.choice(colors)
    new_turtle.color(timColor)
    colors.remove(timColor)
    new_turtle.penup()
    new_turtle.speed(10)
    new_turtle.goto(x= x_position, y= y_position)
    all_turtles.append(new_turtle)
    y_position += 50


user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

while not user_bet in colors:
    print("Please enter an existing color...")
    user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ").lower()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 8)
        turtle.forward(rand_distance)

        if turtle.xcor() > 180:
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"\n\tYou've win!\n\tYour bet was: the {user_bet.upper()} turtle.\n\tThe winner is: the {winning_color.upper()} turtle!")
            else:
                print(f"\n\tYou've lost!\n\tYour bet was: the {user_bet.upper()} turtle.\n\tThe winner is: the {winning_color.upper()} turtle!")

            is_race_on = False

















screen.exitonclick()
