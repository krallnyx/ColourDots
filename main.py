import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()


def draw_line():
    for _ in range(15):
        tim.dot(30, random.randint(10, 245), random.randint(10, 245), random.randint(10, 245))
        tim.forward(50)


def draw_10_lines():
    for _ in range(15):
        draw_line()
        tim.backward(750)
        tim.left(90)
        tim.forward(50)
        tim.right(90)


def init():
    tim.speed(0)
    tim.penup()
    tim.backward(350)
    tim.right(90)
    tim.forward(350)
    tim.left(90)


if __name__ == '__main__':
    init()
    draw_10_lines()
    screen.exitonclick()


