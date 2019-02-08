

# Name: Sandesh Lamichhane

# Doc Link: https://docs.google.com/document/d/1x5rX6GzEgg-MPuUwYkVoDDZmU4mmbn1UQ6iu19AcTMg/edit?usp=sharing


import math
import turtle

wn = turtle.Screen()


def draw_house(house_color, house_height, roof_color):
    """""
    this function will draw a simple square house with a triangle roof
    roof_color is the color of the house roof
    house_color is the color of the house
    house_height is the height of the house
    the house height will be a maximum of ________ to make room for the next function
    """
    pass

    worker_bee.goto(-250, -100)
    worker_bee.pendown()

    # worker_bee draws house
    worker_bee.pencolor(house_color)
    for i in range(4):
        worker_bee.forward(house_height)
        worker_bee.left(90)

    # worker_bee goes to the top of house to draw roof
    worker_bee.left(90)
    worker_bee.fd(house_height)

    # worker bee begins drawing roof
    worker_bee.pencolor(roof_color)
    worker_bee.right(45)
    worker_bee.forward((math.sqrt(house_height**2 + house_height**2))/2)  # pythagorean theorem so that the roof is always perfect
    worker_bee.right(90)
    worker_bee.forward((math.sqrt(house_height**2 + house_height**2))/2)

    # worker_bee goes back to starting place facing the correct place
    worker_bee.penup()
    worker_bee.goto(-250, -100)
    worker_bee.left(45)


def draw_hello(pen_color, pen_size):
    """"
    this function will draw a cursive hello below the house.
    ... hopefully
    pen_color will set the color of the pen
    this function doesn't take any parameters for the actual writing because, honestly, that would be too much work
    """
    pass

    # setting worker_bee position so that it has enough room to draw hello
    worker_bee.right(90)
    worker_bee.fd(200)
    worker_bee.right(180)

    worker_bee.pencolor(pen_color)      # I don't think I need to explain this one
    worker_bee.pensize(pen_size)        # or this one

    # starts drawing
    worker_bee.pendown()

    # draws H
    for i in range(18):     # draws the tiny circle of
        worker_bee.fd(5)
        worker_bee.left(15)

    for i in range(3):      # the beginning of the diagonal line in h
        worker_bee.fd(5)
        worker_bee.left(20)
        worker_bee.fd(15)

    worker_bee.forward(150)

    worker_bee.forward(-85)     # begins the middle section of the H

    worker_bee.right(60)
    worker_bee.forward(75)

    worker_bee.left(60)        # draws the second diagonal line of H
    worker_bee.forward(85)
    worker_bee.forward(-165)

    worker_bee.right(180)

    for i in range(5):      # the end of the second diagonal line in h
        worker_bee.fd(5)
        worker_bee.left(30)
        worker_bee.fd(5)

    # start drawing e
    worker_bee.left(10)
    worker_bee.forward(100)

    for i in range(10):      # draws top curve of e
        worker_bee.fd(5)
        worker_bee.fd(5)
        worker_bee.left(20)

    # for i in range(1):      # draws bottom curve of e
    #     worker_bee.fd(15)
    #     worker_bee.left(35)
    #     worker_bee.fd(15)

    worker_bee.left(15)

    for i in range(6):
        worker_bee.fd(10)
        worker_bee.left(15)
        worker_bee.fd(10)

    # start drawing l

    for i in range(5):
        worker_bee.fd(2)
        worker_bee.fd(2)
        worker_bee.left(15)

    worker_bee.left(5)
    worker_bee.forward(165)
    worker_bee.forward(-165)
    worker_bee.left(180)

    # start the second l
    for i in range(5):
        worker_bee.fd(5)
        worker_bee.fd(5)
        worker_bee.left(40)

    worker_bee.right(20)
    worker_bee.fd(165)
    worker_bee.fd(-165)
    worker_bee.right(180)

    worker_bee.left(100)
    worker_bee.fd(80)

    for i in range(8):
        worker_bee.left(40)
        worker_bee.fd(25)

    # What I really love about read the code and watching the turtle is that you can clearly see when I gave up.


def main():

    # code creating the turtle and setting its attributes.
    global worker_bee
    worker_bee = turtle.Turtle()    # creates a turtle named "worker_bee"
    worker_bee.shape("turtle")
    worker_bee.color("green3")
    worker_bee.pensize("15")
    worker_bee.penup()

    wn.bgcolor("blue")

    draw_house("red", 300, "green")

    draw_hello("red", 5)


main()


wn.exitonclick()
