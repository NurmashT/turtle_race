import turtle as t
from random import randint


screen = t.Screen()
screen.setup(height=600, width=600)
def draw_finish_line():
    tim = t.Turtle()
    tim.penup()
    tim.forward(240)
    tim.pendown()
    tim.left(90)
    tim.forward(250)
    tim.backward(500)
    tim.hideturtle()


colors = ["red", "blue", "orange", "yellow", "purple", "green"]
y_coordinates = [-180, -120, -60, 0, 60, 120]
all_turtles = []
user_guess = screen.textinput(title="Make a bet", prompt="Who is going to win? Enter color: ")

draw_finish_line()

for turtle_index in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.turtlesize(2, 2)
    new_turtle.color("black", colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-270, y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 245:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_guess:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner!")
        distance = randint(1, 10)
        turtle.forward(distance)

screen.exitonclick()