##
# Ben Turner
# A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# references the assignment doc:
# https://docs.google.com/document/d/18mGsKUgGGTHoyN-BFd13Pg0GE5MTkCofZjxaS1oXSR0/edit?usp=sharing
#
# sources used:
# [1] Fibonacci sequence in python using Turtle - https://trinket.io/python/43bc79b582
# [2] Generating a fibonacci sequence in python - https://mortada.net/fibonacci-numbers-in-python.html
#
##

import turtle
from random import randint

# initialize the turtle t and screen wn
t = turtle.Turtle()
wn = turtle.Screen()

# settings

# changes the factor of the side length
f = 1
# speed of the turtle
turtleSpeed = 0

# settings for the colors - boxes, background, and spiral
colors = ["purple", "yellow", "green"]
# set background color to yellow

# end settings
t.speed(turtleSpeed)
wn.bgcolor(colors[1])


def rec_fib(n):
    """a recursive algorithm to generate a fibonacci sequence -- taken almost directly from [2]"""

    if n == 0:  # when n is 0, the next number has to be 0.
        return 0
    elif n == 1:  # when n is 1, the next number is 1
        return 1
    else:  # otherwise, the fibonacci sequence is n-1 + n-2
        return rec_fib(n-1) + rec_fib(n-2)


# generate a fib sequence with a length of 30
fib_seq = ([rec_fib(i) for i in range(randint(10, 20))])
# length of the generated fib sequence
num = len(fib_seq)


def drawsquare(tr, side_len, pencolor):
    """draw a square using turtle tr, with a side length of side_len"""
    tr.pencolor(pencolor)
    for s in range(4):
        tr.forward(side_len)
        tr.right(90)


def drawfib(tr):
    """draw the fibonnaci sequence using squares with a side length equal to the fibonacci numbers"""

    # make sure the pen is up
    tr.penup()
    # go to quadrant A, offset a little
    tr.goto(50, 50)
    # pendown so we are now writing
    tr.pendown()

    # iterate through the fib sequence, and draw the square with the length of that number
    for i in range(num):
        # draw a square with turtle, length of the fib sequence of index i, in the color purple
        drawsquare(tr, f * fib_seq[i], colors[0])
        tr.penup()
        # move forward the same amount, turn 90 degrees to the right, and move forward again
        tr.fd(f * fib_seq[i])
        tr.right(90)
        tr.fd(f * fib_seq[i])
        tr.pendown()
    # set the penup since we're done with it now.
    tr.penup()


def drawcir(tr):
    """draws a series of quarter circles, showing the fibonnaci spiral, using the turtle tr"""

    tr.penup()

    # move the turtle to quadrant A, so it's off center a little bit, at coordinates 50, 50
    tr.goto(50, 50)
    # set the heading to 0
    tr.seth(0)
    # change the pencolor to green
    tr.pencolor(colors[2])
    # increase the pensize a bit
    tr.pensize(5)
    tr.pendown()
    # draw 90 degrees (a quarter) of a circle, with the radius of the number in the fib sequence
    # multiplied by a negative factor, so it draws in the clockwise direction
    for i in range(num):
        tr.circle(-f * fib_seq[i], 90)


def main():
    """main method, lets us run all the methods at once, in the correct order"""
    drawfib(t)
    drawcir(t)
    # keeps the screen open once finished, so that it doesn't close unless you close it
    turtle.done()


# run the main method
main()
