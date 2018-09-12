#################################################################################
# Authors: Emily Lovell & Scott Heggen
# usernames: lovelle & heggens
#
# A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
#
# Showing an example of a branch already created.
#################################################################################
# Acknowledgement
#
# Original code by Scott Heggen and Emily Lovell
#
#################################################################################


import turtle                   # allows us to use the turtles library


def setup_turtle(tess):
    """
    Sets up the turtle for drawing

    :param tess: a turtle object
    :return: None
    """
    tess.color("blue")              # Tell tess to change her color
    tess.pensize(3)                 # Tell tess to set her pen width
    tess.penup()
    tess.goto(tess.xcor()-100, tess.ycor()+50)
    tess.pendown()


def draw_S(tess):
    """
    Draws an S
    :param tess: a turtle object
    :return: None
    """
    tess.left(180)
    tess.fd(20)
    tess.left(90)
    tess.fd(40)
    tess.left(90)
    tess.fd(20)
    tess.right(90)
    tess.fd(40)
    tess.right(90)
    tess.fd(20)


def draw_move_to_H(tess):
    """
    Moves to the start of the H
    :param tess: a turtle object

    :return: None
    """
    tess.penup()
    tess.goto(tess.xcor()+40, tess.ycor()+50)
    tess.pendown()


def draw_H(tess):
    """
    Draws an H

    :param tess: a turtle object
    :return: None
    """
    # draw H
    tess.setheading(270)
    tess.fd(80)
    tess.backward(40)
    tess.left(90)
    tess.fd(20)
    tess.left(90)
    tess.fd(40)
    tess.backward(80)


def draw_move_to_E(tess):
    """
    Moves to the start of the E

    :param tess: a turtle object
    :return: None
    """
    tess.penup()
    tess.goto(tess.xcor()+20, tess.ycor()+110)
    tess.pendown()


def draw_E(tess):
    """
    Draws an E

    :param tess: a turtle object
    :return: None
    """
    tess.setheading(0)
    tess.fd(20)
    tess.bk(20)
    tess.right(90)
    tess.fd(40)
    tess.left(90)
    tess.fd(15)
    tess.bk(15)
    tess.right(90)
    tess.fd(40)
    tess.left(90)
    tess.fd(20)


def draw_move_to_L(tess):
    """
    Moves to the start of the L

    :param tess: a turtle object
    :return: None
    """
    tess.penup()
    tess.goto(tess.xcor()+20, tess.ycor()+50)
    tess.pendown()


def draw_L(tess):
    """
    Draws an L

    :param tess: a turtle object
    :return: None
    """
    tess.setheading(270)
    tess.fd(80)
    tess.left(90)
    tess.fd(20)


def draw_move_to_border(tess):
    """
    Moves to the start of the border

    :param tess: a turtle object
    :return: None
    """
    tess.penup()
    tess.goto(tess.xcor()+20, tess.ycor()+150)


def draw_border(tess):
    """
    Draws the pink border

    :param tess: a turtle object
    :return: None
    """
    tess.shape("turtle")
    tess.color("pink")
    tess.seth(180)
    for i in range(4):
        for i in range(9):
            tess.stamp()
            tess.fd(20)
        tess.left(90)


def draw_border_2(tess):
    """
    Draws the black border

    :param tess: a turtle object
    :return: None
    """
    tess.shape("arrow")
    tess.goto(tess.xcor()+20, tess.ycor()+20)
    tess.color("black")
    for i in range(4):
        for i in range(9):
            tess.stamp()
            tess.fd(25)
        tess.left(90)


def spawn_turtles():
    """
    Creates four new turtle objects

    :return: a tuple of four turtle objects
    """
    tess1 = turtle.Turtle()
    tess2 = turtle.Turtle()
    tess3 = turtle.Turtle()
    tess4 = turtle.Turtle()
    return (tess1, tess2, tess3, tess4)


def draw_arms(tess1, tess2, tess3, tess4):
    """
    Draws four arms from each corner

    :param tess1: a turtle object
    :param tess2: a turtle object
    :param tess3: a turtle object
    :param tess4: a turtle object
    :return: None
    """
    for i in range(9):
        tess1.stamp()
        tess1.fd(30)
        tess1.right(15)
        tess2.stamp()
        tess2.fd(30)
        tess2.right(15)
        tess3.stamp()
        tess3.fd(30)
        tess3.right(15)
        tess4.stamp()
        tess4.fd(30)
        tess4.right(15)


def create_legs(tess):
    """
    Sets up the creation of the four legs

    :param tess: a turtle object
    :return: None
    """

    # Calls the spawn_turtles() function, and saves the return value to four turtles
    (tess1, tess2, tess3, tess4) = spawn_turtles()

    # Setup up tess1
    tess1.penup()
    tess1.color("red")
    tess1.goto(tess.xcor()+20, tess.ycor()-12*20)
    tess1.seth(315)

    # Setup up tess2
    tess2.penup()
    tess2.color("red")
    tess2.goto(tess.xcor()-12*20, tess.ycor()+20)
    tess2.seth(135)

    # Setup up tess3
    tess3.penup()
    tess3.color("red")
    tess3.goto(tess.xcor()+20, tess.ycor()+20)
    tess3.seth(45)

    # Setup up tess4
    tess4.penup()
    tess4.color("red")
    tess4.goto(tess.xcor()-12*20, tess.ycor()-12*20)
    tess4.seth(225)

    draw_arms(tess1, tess2, tess3, tess4)       # calls the draw_arms function, and passes it the four turtles


def main():
    """
    Uses multiple functions to draw a pretty picture.

    :return: None
    """
    wn = turtle.Screen()            # creates a graphics window--needed for a clean close

    wn.bgcolor("lightgreen")        # Set the window background color
    wn.title("Hello, Class!")       # Set the window title

    shelly = turtle.Turtle()        # create a turtle named tess

    setup_turtle(shelly)            # calls the function setup_turtle(). Passes the turtle object to the function
    draw_S(shelly)                  # calls the function draw_S(). Passes the turtle object to the function
    draw_move_to_H(shelly)          # .
    draw_H(shelly)                  # .
    draw_move_to_E(shelly)          # .
    draw_E(shelly)
    draw_move_to_L(shelly)
    draw_L(shelly)
    draw_move_to_border(shelly)
    draw_border(shelly)
    draw_border_2(shelly)
    create_legs(shelly)

    wn.exitonclick()                # for clean closing of the Screen


main()

