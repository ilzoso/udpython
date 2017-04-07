import turtle
import math
import time

def draw_triangle(ass, x1, x2, y1, y2, inverted):
    print "drawing triangle ", x1, x2, y1, y2, inverted
    if not inverted:
        ass.color(1, 1, 1)
        ass.setpos(x1, y1)
        ass.color(0, 0, 0)
        ass.setheading(0)
        #ass.fillcolor(0.5, 0.2, 0.7)
        ass.forward(x2-x1)
        ass.left(120)
        ass.forward(x2-x1)
        ass.left(120)
        ass.forward(x2-x1)
    else:
        ass.color(1, 1, 1)
        ass.setpos(x1, y2)
        ass.color(0, 0, 0)
        ass.setheading(0)
        ass.forward(x2-x1)
        ass.right(120)
        ass.forward(x2-x1)
        ass.right(120)
        ass.forward(x2-x1)

def process_triangle(ass, x1, x2, y1, y2, isInverted):
    # draw one triangle !isInverted
    print "process triangle ", x1, x2, y1, y2, isInverted
    if x2-x1 > 10:
        if isInverted:
            x2_1, x2_2 = x1, x1 + (x2 - x1) * 0.50
            x1_1, x1_2 = x1 + (x2 - x1) * 0.25, x1 + (x2 - x1) * 0.75
            x4_1, x4_2 = x1 + (x2 - x1) * 0.50, x2
            x3_1, x3_2 = x1 + (x2 - x1) * 0.25, x1 + (x2 - x1) * 0.75
            y2_1, y2_2 = y1 + (y2 - y1) * 0.50, y2
            y1_1, y1_2 = y1, y1 + (y2 - y1) * 0.50
            y4_1, y4_2 = y1 + (y2 - y1) * 0.50, y2
            y3_1, y3_2 = y1 + (y2 - y1) * 0.50, y2
        else:
            x2_1, x2_2 = x1, x1 + (x2 - x1) * 0.50
            x1_1, x1_2 = x1 + (x2 - x1) * 0.25, x1 + (x2 - x1) * 0.75
            x4_1, x4_2 = x1 + (x2 - x1) * 0.50, x2
            x3_1, x3_2 = x1 + (x2 - x1) * 0.25, x1 + (x2 - x1) * 0.75
            y2_1, y2_2 = y1, y1 + (y2 - y1) * 0.50
            y1_1, y1_2 = y1 + (y2 - y1) * 0.50, y2
            y4_1, y4_2 = y1, y1 + (y2 - y1) * 0.50
            y3_1, y3_2 = y1, y1 + (y2 - y1) * 0.50
        draw_triangle(ass, x3_1, x3_2, y3_1, y3_2, not isInverted)
        process_triangle(ass, x1_1, x1_2, y1_1, y1_2, isInverted)
        process_triangle(ass, x2_1, x2_2, y2_1, y2_2, isInverted)
        #process_triangle(ass, x3_1, x3_2, y3_1, y3_2, not isInverted)
        process_triangle(ass, x4_1, x4_2, y4_1, y4_2, isInverted)

def draw_fractal(size = 300, x = 0, y = 0, isInverted = False):
    ass = turtle.Turtle()
    ass.shape("arrow")
    ass.speed(10)
    w = size * 1.0
    h = size * 1.0 * math.sqrt(3) / 2
    x1 = x * 1.0
    x2 = x * 1.0 + size
    y1 = y * 1.0
    y2 = y * 1.0 + size * math.sqrt(3) / 2
    print x1, x2, y1, y2
    draw_triangle(ass, x1, x2, y1, y2, isInverted)
    process_triangle(ass, x1, x2, y1, y2, isInverted)


draw_fractal()
window = turtle.Screen()
window.exitonclick()


#1 draw draw_triangle
#2 draw inverted mid triangle
#3 call 2 for 4 resulting triangles - 3 same direction, 1 inverted

