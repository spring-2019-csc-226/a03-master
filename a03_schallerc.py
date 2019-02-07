# Author: Caleb Schaller
# Username: Schallerc
# A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# https://docs.google.com/document/d/1LndrCptToRmX_Qy5MglTEVmnpXgzEwnNfTUm3XrSkdc/edit?usp=sharing


import turtle



def main_house(r):
    """
    Docstring for function_1
    """

    for i in range(4):
        r.forward(100)
        r.left(90)

def chimney(t):
    """
    Docstring for function_2
    """
    for i in range(4):
        t.left(90)
        t.forward(70)

def window(y):
    """
    Docstring for function_3
    """
    for i in range(1):
        y.penup()
        y.forward(50)
        y.pendown()
        y.left(90)
        y.forward(20)
        y.left(90)
        y.forward(10)
        y.left(90)
        y.forward(20)


def main():
    """
    Docstring for main
    """
    # ...

    wn = turtle.Screen()  # makes a new turtle screen
    wn.bgcolor("red")
    r = turtle.Turtle
    t = turtle.Turtle
    y = turtle.Turtle
    main_house(r)  # Function call to function_1
    chimney(t)  # Function call to function_2
    window(y)  # Function call to function_3

    wn.exitonclick()

main()
