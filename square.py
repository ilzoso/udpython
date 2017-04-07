import turtle
import math
import time

def draw_square():
    window = turtle.Screen()
    window.bgcolor(.5,0,0)
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(10)
    for xx in range(0, 36):
        colr1 = float(xx)/35
        colr2 = float(35-xx)/35
        brad.color((1, colr1, colr2))
        for yy in range(0, 4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
    window.exitonclick()


draw_square()

