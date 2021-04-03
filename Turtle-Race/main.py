from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
bet_color = screen.textinput(title='Make a Bet',
                             prompt='Which turtle will win the race? (Red, Blue, Green, Yellow, Purple, orange')
colours = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
y_cord = [-70, -40, -10, 20, 50, 80]
turtle_list = []
for i in range(0, 6):
    turtle = Turtle(shape='turtle')
    turtle.penup()
    turtle.color(colours[i])
    turtle.goto(-240, y_cord[i])
    turtle_list.append(turtle)

race_is_on = True
while race_is_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_is_on = False
            if turtle.pencolor() == bet_color:
                print(f'You win!! The {turtle.pencolor()} is the winner')
            else:
                print(f'You lost!! The {turtle.pencolor()} is the winner')
            break
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
