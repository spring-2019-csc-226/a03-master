##
# Ben Turner
# A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# references the assignment doc:
# https://docs.google.com/document/d/18mGsKUgGGTHoyN-BFd13Pg0GE5MTkCofZjxaS1oXSR0/edit?usp=sharing
# inspiration and ideas from the following sources:
# Fibonacci sequence in python using Turtle - https://trinket.io/python/43bc79b582
# Generating a fibonacci sequence in python - https://mortada.net/fibonacci-numbers-in-python.html
#
##

import turtle
from random import randint

# initialize the turtle t and screen wn
t = turtle.Turtle()
wn = turtle.Screen()
# set background color to yellow
wn.bgcolor("yellow")


def rec_fib(n):
    # recursive algorithm to generate a fibonacci sequence
    if n == 0:  # when n is 0, the next number has to be 0.
        return 0
    elif n == 1:  # when n is 1, the next number is 1
        return 1
    else:  # otherwise, the fibonacci sequence is n-1 + n-2
        return rec_fib(n-1) + rec_fib(n-2)


# generate a fib sequence with a length of 30
fibseq = ([rec_fib(i) for i in range(randint(10, 20))])


def dwsquare(tr, side_len, pencolor):
    # draw a square using turtle tr, with a side length of side_len
    tr.pencolor(pencolor)
    for s in range(4):
        tr.forward(side_len)
        tr.right(90)

def drawfib(tr):
    # draw the fibonnaci sequence using squares with a side length equal to the fibonacci numbers

    # make sure the pen is up
    tr.penup()
    # go to quadrant A, offset a little
    tr.goto(50, 50)
    # pendown so we are now writing
    tr.pendown()

    # iterate through the fib sequence, and draw the square with the length of that number
    for i in range(num):
        dwsquare(tr, n*fibseq[i], "purple")
        tr.penup()
        tr.fd(n * fibseq[i])
        tr.right(90)
        tr.fd(n * fibseq[i])
        tr.pendown()
    # set the penup since we're done with it now.
    tr.penup()


def drawcir(tr):
    # draws a series of quarter circles, showing the fibonnaci spiral, using the turtle tr

    tr.penup()
    tr.goto(50, 50)
    tr.seth(0)
    tr.pencolor('green')
    tr.pensize(5)
    tr.pendown()

    for i in range(num):
        tr.circle(-n*fibseq[i], 90)

# initialize constants
num = len(fibseq)
# changes the factor of the side length
n = 1
# speed of the turtle
t.speed(0)


def main():
    # main method, lets us 
    drawfib(t)
    drawcir(t)
    turtle.done()

main()
