import logging
from turtle import Turtle, Screen

logging.basicConfig(level = logging.DEBUG)

tim = Turtle()
scr = Screen()
angle = 0


def move_forwards():
    tim.forward(10)


def move_backwards():
    turn_around()
    tim.forward(10)


def turn_left():
    global angle
    angle += 10
    tim.setheading(angle)


def turn_right():
    global angle
    angle -= 10
    tim.setheading(angle)


def turn_around():
    tim.setheading(180)


def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


def main():
    scr.listen()
    scr.onkey(key = "w", fun = move_forwards)
    scr.onkey(key = "s", fun = move_backwards)
    scr.onkey(key = "a", fun = turn_left)
    scr.onkey(key = "d", fun = turn_right)
    scr.onkey(key = "c", fun = clear)

    scr.exitonclick()


if __name__ == '__main__':

    main()

# logging.debug(stuff)
