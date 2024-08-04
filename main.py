from turtle import Turtle, Screen
import turtle as tur

tim = Turtle()
screen = Screen()


tim.shape("classic")
tim.color("green")
tim.pensize(2)
tim.shapesize(1.5)

def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_clock():
    tim.right(10)


def turn_anticlock():
    tim.left(10)


def penup():
    tim.penup()


def pendown():
    tim.pendown()


def clear_draw():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    tim.pencolor("green")
    tim.shapesize(1.5)
    tim.pensize(2)


def erase():
    tim.pendown()
    tim.pensize(25)
    tim.shapesize(2)
    tim.pencolor("black")


def draw():
    tim.pensize(2)
    tim.color("green")
    tim.shapesize(1.5)

tur.title("Sketch It")
screen.bgcolor("black")
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=turn_clock)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_anticlock)
screen.onkey(key="q", fun=penup)
screen.onkey(key="e", fun=pendown)
screen.onkey(key="c", fun=clear_draw)
screen.onkey(key="f", fun=erase)
screen.onkey(key="r", fun=draw)
screen.exitonclick()
