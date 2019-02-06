################################################################################
# Author:Justin Vankirk
# Username:vankirkj
#
# Assignment:A03
# https://docs.google.com/document/d/1upvTP9Z7BehzY-HqRqI9Uh2F3cD19rZi_MtArv0Tn_M/edit?usp=sharing
#################################################################################
# Acknowledgements: Azah and I made the stars
#
#
#################################################################################

import turtle


def makesquare():   #makes the square outline
    square = turtle.Turtle()
    square.penup()
    square.setpos(-241, 241)
    square.pendown()
    square.pensize(20)
    square.color("white")
    for i in range(4):
        square.forward(500)
        square.right(90)



    """
    Docstring for function_1
    """
    # ...


def boustraphedon():
    fanciness = turtle.Turtle()     #stars!!!
    fanciness.pensize(20)
    fanciness.penup()
    fanciness.setpos(-221, 221)
    fanciness.pendown()
    fanciness.speed(100)
    for i in range(5):                       ###This is the algorythm for our stars.###
        for i in range(11):
            fanciness.forward(20)
            fanciness.right(90)
            fanciness.forward(20)
            fanciness.right(90)
            fanciness.forward(20)
            fanciness.left(90)
            fanciness.forward(20)
            fanciness.left(90)
        fanciness.forward(20)
        fanciness.right(90)
        fanciness.forward(20)
        fanciness.right(90)
        fanciness.forward(20)
        fanciness.right(180)
        fanciness.forward(60)
        fanciness.left(180)
        for i in range(11):
            fanciness.forward(20)
            fanciness.right(90)
            fanciness.forward(20)
            fanciness.right(90)
            fanciness.forward(20)
            fanciness.left(90)
            fanciness.forward(20)
            fanciness.left(90)
        fanciness.forward(20)
        fanciness.right(90)
        fanciness.forward(20)
        fanciness.right(90)
        fanciness.forward(20)
        fanciness.right(180)
        fanciness.backward(20)
        fanciness.left(180)
    for i in range(11):                   #if we continued this last loop, it would be impossible to keep the snake inside the box.
        fanciness.forward(20)             #We subtracted this last line of code in order to fix it.
        fanciness.right(90)
        fanciness.forward(20)
        fanciness.right(90)
        fanciness.forward(20)
        fanciness.left(90)
        fanciness.forward(20)
        fanciness.left(90)
    fanciness.forward(20)
    fanciness.right(90)
    fanciness.forward(20)
    fanciness.right(90)
    fanciness.forward(20)
    fanciness.right(180)
    fanciness.forward(60)
    fanciness.left(180)
    for i in range(11):
        fanciness.forward(20)
        fanciness.right(90)
        fanciness.forward(20)
        fanciness.right(90)
        fanciness.forward(20)
        fanciness.left(90)
        fanciness.forward(20)
        fanciness.left(90)
    fanciness.forward(20)
    fanciness.right(90)
    fanciness.forward(20)
    fanciness.right(90)
    fanciness.forward(20)
    fanciness.right(180)
    fanciness.left(180)






    """
    Create the background
    """

    # ...


def makeskyscraper():
    skyscraper = turtle.Turtle()    #makes the skyscrapers base
    skyscraper.color(115,115,200)
    skyscraper.width(10)
    skyscraper.penup()
    skyscraper.setpos(-100,-245)
    skyscraper.pendown()
    skyscraper.begin_fill()
    skyscraper.forward(100)
    skyscraper.left(90)
    skyscraper.forward(400)
    skyscraper.left(90)
    skyscraper.forward(100)
    skyscraper.left(90)
    skyscraper.forward(400)
    skyscraper.end_fill()


def door():
    door = turtle.Turtle()        #skyscraper door
    door.penup()
    door.setpos(-75, -245)
    door.pendown()
    door.begin_fill()
    for i in range(2):
        door.forward(30)
        door.left(90)
        door.forward(50)
        door.left(90)
    door.end_fill()
    door.hideturtle()


def main():
    """
    This actually runs the code.
    """
    # ...
    makesquare()            # Function call to function_1
    boustraphedon()            # Function call to function_2
    makeskyscraper()
    door()


window = turtle.Screen()
window.bgcolor("yellow")
window.colormode(255)
main()
window.exitonclick()