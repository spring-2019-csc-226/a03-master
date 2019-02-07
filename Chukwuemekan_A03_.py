######################################################################
# Author: Emily Lovell & Scott Heggen        TODO: Change this to your name, if modifying
# Username: lovelle & heggens                TODO: Change this to your username, if modifying
#

# Assignment: A02: Loopy Turtles, Loopy Languages
# Purpose: Draws a 3D cube using turtles and nested for loops
######################################################################
# Acknowledgements:

# Original code by: Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle

wn = turtle.Screen()
wn.bgcolor("pink")
yugi = turtle.Turtle()
yugi.pencolor("black")

def draw_cute_shape(length, yugi):
    """This draws the inner shape which is the 'nose' """
    yugi.penup()
    yugi.goto(0,30)
    yugi.pendown()
    yugi.pensize(10)
    for i in range(6):
        yugi.forward(length)
        yugi.right(60)

def another_shape(length, yugi):
    """This draws the shape by the top left which is the eye"""
    yugi.pensize(5)
    yugi.penup()
    yugi.goto(-65,100)
    yugi.pendown()
    for i in range(9):
        yugi.forward(length)
        yugi.right(40)


def another_shape_again(length, yugi):
    yugi.pensize(5)
    yugi.penup()
    yugi.goto(-65,-120)
    yugi.pendown()
    for i in range(9):
        yugi.forward(length)
        yugi.right(40)


def next_shape(length, yugi):
    yugi.pensize(5)
    yugi.penup()
    yugi.goto(120,100)
    yugi.pendown()
    for i in range(9):
        yugi.forward(length)
        yugi.right(40)


def next_shape_again(length, yugi):
    yugi.pensize(5)
    yugi.penup()
    yugi.goto(120,-120)
    yugi.pendown()
    for i in range(9):
        yugi.forward(length)
        yugi.right(40)
    yugi.penup()


def draw_smile(length, yugi):
    """This draws the smile/the mouth"""
    yugi.penup()
    yugi.goto(-100,-215)
    yugi.pendown()
    yugi.right(42)
    yugi.forward(length)
    yugi.left(42)
    yugi.forward(180)
    yugi.left(40)
    yugi.forward(length)


def draw_circle():
    """This draws the head"""
    yugi.penup()
    yugi.goto(230,-260)
    yugi.pendown()
    yugi.circle(280)
    yugi.penup()
    yugi.goto(240,-270)
    yugi.write("I am a human face but not a human face", move="false",align ="left",font=("arial", 16, "normal")) #This line writes on the screen

def main():
    draw_cute_shape(100, yugi)
    another_shape(35, yugi)
    another_shape_again(35, yugi)
    next_shape(35, yugi)
    next_shape_again(35, yugi)
    draw_smile(80, yugi)
    draw_circle()
main()

wn.exitonclick()





