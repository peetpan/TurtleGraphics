from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.setheading(90)


def moveforward():
    turtle.forward(20)


def movebackward():
    turtle.back(20)


def turnleft():
    turtle.left(20)


def turnright():
    turtle.right(20)


def reset():
    screen.reset()


screen.listen()
screen.onkey(key='Up', fun=moveforward)
screen.onkey(key='Down', fun=movebackward)
screen.onkey(key='Left', fun=turnleft)
screen.onkey(key='Right', fun=turnright)
screen.onkey(key='c', fun=reset)

screen.exitonclick()
