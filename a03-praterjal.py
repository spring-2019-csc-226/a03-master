# Author: Jalen Prater
# Username: praterjal
# Google Doc: https://docs.google.com/document/d/1ZIEFRlNIQKXA2H3r_NANiNE1lOZInasV8zJ4QTQ9550/edit?usp=sharing
# Assignment: a03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: to draw house
######################################################################

import turtle
def draw():
    screen1 = turtle.Screen()
    screen1.bgcolor("blue")
    alex = turtle.Turtle()
    alex.color("#010601")
    alex.pensize(10)
    alex.pendown()
    alex.forward(120)
    alex.left(90)
    alex.forward(150)
    alex.left(90)
    alex.forward(120)
    alex.left(90)
    alex.forward(150)
    alex.left(90)
    alex.forward(120)
    alex.left(90)
    alex.forward(10)
    alex.right(90)
    alex.forward(130)
    alex.left(90)
    alex.forward(120)
    alex.left(90)
    alex.forward(130)
    alex.right(90)
    alex.forward(20)
    alex.left(45)
    alex.forward(87)
    alex.left(90)
    alex.forward(82)
    alex.left(45)
    alex.forward(20)
    alex.right(90)
    alex.forward(130)
    alex.left(90)
    alex.forward(120)
    alex.left(90)
    alex.forward(130)
    alex.left(90)
    alex.forward(95)
    alex.right(90)

    alex.penup()


    alex.forward(10)
    alex.pendown()
    alex.pensize(5)
    alex.forward(20)
    alex.left(90)
    alex.forward(30)
    alex.left(90)
    alex.forward(20)
    alex.left(90)
    alex.forward(30)

    alex.penup()

    alex.left(90)
    alex.forward(75)

    alex.pendown()
    alex.forward(20)
    alex.left(90)
    alex.forward(30)
    alex.left(90)
    alex.forward(20)
    alex.left(90)
    alex.forward(30)

    alex.penup()

    alex.right(90)
    alex.forward(15)
    alex.left(90)
    alex.forward(55)

    alex.pendown()
    alex.right(90)
    alex.forward(25)
    alex.left(90)
    alex.forward(55)
    alex.left(90)
    alex.forward(25)
    alex.left(90)
    alex.forward(55)
    screen1.exitonclick()
def main():
    draw()
main()








