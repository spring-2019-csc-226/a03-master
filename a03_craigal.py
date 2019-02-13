#################################################################################
# Author: Alexander Craig
# Username: craigal
#
# Assignment: A03 A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To create a a complex thing which looks like something
# Link: https://docs.google.com/document/d/12bwYDe89hLwqkxCrZrqCdVmUnfAmKloB1LQqcxianMM/edit?usp=sharing
#################################################################################
import turtle
wn = turtle.Screen()
wn.colormode(255)
my_turtle = turtle.Turtle()
wn.screensize(750, 750)     # changes the window size
wn.bgcolor(14, 122, 13)     # changes the background to xbox green


def function_1():       # draws the 2-D base of the front of the xbox
    my_turtle.penup()
    my_turtle.begin_fill()
    my_turtle.color(0, 0, 0)
    my_turtle.setpos(-100, 0)
    my_turtle.pendown()
    for side in range(2):
        my_turtle.forward(333)
        my_turtle.right(90)
        my_turtle.forward(79)
        my_turtle.right(90)
    my_turtle.end_fill()


def function_2():       # Draws the power button
    my_turtle.begin_fill()
    my_turtle.color(255, 255, 255)
    my_turtle.penup()
    my_turtle.setpos(200, -50)
    my_turtle.pendown()
    my_turtle.circle(10)
    my_turtle.end_fill()


def function_3():       # draws the outside of the disc tray
    my_turtle.begin_fill()
    my_turtle.color(100, 100, 100)
    my_turtle.penup()
    my_turtle.setpos(-100, -32.5)
    my_turtle.pendown()
    for side in range(2):
            my_turtle.forward(166.5)
            my_turtle.right(90)
            my_turtle.forward(14)
            my_turtle.right(90)
    my_turtle.end_fill()


def function_4():       # Draws the inside of the disc tray
    my_turtle.begin_fill()
    my_turtle.color(0, 0, 0)
    my_turtle.penup()
    my_turtle.setpos(-90, -34.5)
    my_turtle.pendown()
    for side in range(2):
        my_turtle.forward(150)
        my_turtle.right(90)
        my_turtle.forward(10)
        my_turtle.right(90)
    my_turtle.end_fill()


def function_5():   # Draws the top of the xbox in black, and right side of the xbox in dark gray for shading
    my_turtle.penup()
    my_turtle.begin_fill()
    my_turtle.color(0, 0, 0)
    my_turtle.setpos(-100, 0)
    my_turtle.pendown()
    my_turtle.left(45)
    my_turtle.forward(137)
    my_turtle.right(45)
    my_turtle.forward(333)
    my_turtle.right(135)
    my_turtle.forward(137)
    my_turtle.right(45)
    my_turtle.forward(333)
    my_turtle.end_fill()
    my_turtle.begin_fill()
    my_turtle.color(52, 52, 52)
    my_turtle.penup()
    my_turtle.setpos(233, -79)
    my_turtle.pendown()
    my_turtle.right(135)
    my_turtle.forward(137)
    my_turtle.left(45)
    my_turtle.forward(79)
    my_turtle.left(135)
    my_turtle.forward(137)
    my_turtle.left(45)
    my_turtle.forward(79)
    my_turtle.end_fill()


def main():     # Calls all of the functions
    function_1()
    function_2()
    function_3()
    function_4()
    function_5()


main()
wn.exitonclick()
