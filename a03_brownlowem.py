#################################################################################################################
# Author: Kenzie Brownlowe
# Username: brownlowem
# Google Doc link: https://docs.google.com/document/d/1GsYXfooStfNguOEsKxxRiVf-bnGF4GDo-3OJGRuzfFc/edit?usp=sharing
#################################################################################################################


import turtle
wn = turtle.Screen()
wn.bgcolor('lightblue')


def function_1(house):
    """
    draws the square house
    """
    house.penup()
    house.goto(200, -250)
    house.pendown()
    house.begin_fill()
    for i in range(4):
        house.left(90)
        house.forward(400)
    house.end_fill()


def draw_attributes(attributes):
    """""
    Drawing the roof and the door
    """
    attributes.penup()
    attributes.goto(250, 150)
    attributes.pendown()
    attributes.begin_fill()
    attributes.left(120)
    attributes.forward(100)
    attributes.left(60)
    attributes.forward(400)
    attributes.left(60)
    attributes.forward(100)
    attributes.left(120)
    attributes.forward(500)
    attributes.end_fill()
    attributes.penup()
    attributes.goto(50, -250)
    attributes.pendown()
    attributes.begin_fill()
    for i in range(2):
        attributes.left(90)
        attributes.forward(200)
        attributes.left(90)
        attributes.forward(100)
    attributes.end_fill()


def draw_windows(window, x, y):
    """""
    Draws both of the square windows and I give the coordinates.
    """
    window.penup()
    window.goto(x, y)
    window.pendown()
    window.begin_fill()
    window.fillcolor('lightblue')
    for i in range(4):
        window.forward(75)
        window.left(90)
    window.end_fill()
    window.forward(37.5)
    window.left(90)
    window.forward(75)
    window.left(90)
    window.forward(37.5)
    window.left(90)
    window.forward(37.5)
    window.left(90)
    window.forward(75)


def main():
    house = turtle.Turtle()
    house.color('white')
    house.pensize(5)
    house.shape('circle')
    function_1(house)
    turtle.colormode(255)
    attributes = turtle.Turtle()
    attributes.color(255, 0, 0)
    draw_attributes(attributes)
    window = turtle.Turtle()
    window.color('black')
    window.pensize(3)
    draw_windows(window, 75, -50)
    draw_windows(window, -150, 0)


main()


wn.exitonclick()
