######################################################################
# Author: Opaleye Joseph
# Username: opaleyej
#GoogleDoc: https://docs.google.com/document/d/1nBNPwKARiT_e2YdZs-gvhHViqKS7DYVTNAS-d8UxQkw/edit?usp=sharing
#
# Assignment: A3: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
######################################################################

import turtle


def make_turtle(color):
    """
    Make a turtle
    :param color: gives color of turtle
    :return: turtle object
    """
    joe = turtle.Turtle()
    joe.color(color)
    joe.pensize(5)
    joe.speed(10)
    joe.hideturtle()
    return joe

def set_turtle(house1, heat1, heat2):
    """
    Allow turtle to start drawing
    :param name: name of the
    :param heat1:
    :param heat2:
    :return: none
    """
    house1.penup()
    house1.goto(heat1, heat2)
    house1.pendown()


def make_rectangle(house2, side1, side2):
    """
    Draw rectangle
    :param name: naming the turtle drawing
    :param side1: one side of the rectangle
    :param side2: other side of rectangle
    :return: none
    """
    for rectangles in range(2):
        house2.forward(side1)
        house2.left(90)
        house2.forward(side2)
        house2.left(90)


def make_trianlge(joehouse, side1):
    """
    To make a triangle
    :param name: is the name of the turtle drawing
    :param side1: sides of the triangle
    :return: none
    """
    for tri in range(3):
        joehouse.forward(side1)
        joehouse.left(120)

def main():
    wn = turtle.Screen()            # creates a screen
    wn.bgpic("field.png")           # creates a field background

    tayo = make_turtle('brown')     # draw the foundation of the house
    tayo.begin_fill()
    wn.colormode(255)
    tayo.fillcolor((110, 15, 20))   # make an rgb color
    set_turtle(tayo, -330, -280)
    make_rectangle(tayo, 300, 300)
    tayo.end_fill()

    chimney = make_turtle('brown')     # draw chimney
    chimney.begin_fill()
    set_turtle(chimney, -98, 25)
    make_rectangle(chimney, 50, 150)
    chimney.end_fill()

    lagos = make_turtle('black')     # draw a roof
    set_turtle(lagos, -330, 20)
    lagos.fillcolor('black')
    lagos.begin_fill()
    make_trianlge(lagos, 300)
    lagos.end_fill()

    moor = make_turtle('black')     # draw a door
    moor.begin_fill()
    set_turtle(moor, -140, -270)
    make_rectangle(moor, 100, 200)
    moor.end_fill()
    make_trianlge(lagos, 300)
    lagos.end_fill()

    window1 = make_turtle('black')     # make the frame for window
    window1.begin_fill()
    window1.fillcolor('white')
    set_turtle(window1, -320, -160)
    make_rectangle(window1, 70, 100)
    window1.end_fill()

    set_turtle(window1, -320, -160)     # make window separation
    make_rectangle(window1, 70, 50)

    set_turtle(window1, -320, -160)    # make window separation
    make_rectangle(window1, 35, 100)

    doorknob = make_turtle('white')     # make doorknob to door
    doorknob.shape('circle')
    set_turtle(doorknob, -55, -180)
    doorknob.stamp()
    wn.exitonclick()                # end on click


main()
