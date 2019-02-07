#################################################################################
#  Author: Mahmoud Amer
# Username: Amerm
#
# Assignment: A03
#
#################################################################################


import turtle


def draw_square(sz, t):
    """
    This function draws a square
    """
    for i in range(4):
        t.forward(sz)
        t.left(90)


def draw_triangle(t):
    """
    This function draws a triangle
    """
    for i in range(3):
        t.forward(200)
        t.left(120)


def main():

    wn = turtle.Screen()
    wn.bgcolor("#8eb9ff")
    tess = turtle.Turtle()
    tess.color("red")
    tess.right(90)
    tess.forward(100)
    tess.left(90)
    tess.fillcolor("red")
    tess.begin_fill()
    draw_square(200, tess)
    tess.end_fill()
    tess.left(90)
    tess.forward(200)
    tess.right(90)
    tess.color("green")
    tess.begin_fill()
    draw_triangle(tess)
    tess.end_fill()
    tess.penup()
    tess.right(90)
    tess.forward(80)
    tess.left(90)
    tess.forward(20)
    tess.color("blue")
    tess.pendown()
    tess.begin_fill()
    draw_square(50,tess)
    tess.end_fill()
    tess.penup()
    tess.forward(100)
    tess.begin_fill()
    draw_square(50,tess)
    tess.end_fill()
    tess.right(90)
    tess.forward(120)
    tess.left(90)
    tess.forward(-60)
    tess.color("brown")
    tess.pendown()
    tess.begin_fill()
    draw_square(70,tess)
    tess.end_fill()
    wn.exitonclick()


main()
