#################################################################################
# Author: Eleni Lazaridou
# Username: lazaridoue
#Google DOC URL: https://docs.google.com/document/d/11Y7FZvrbtlYuThrtih7vINCvpzBI3kb0Ik2p6TMyOk8/edit?usp=sharing
#
# Assignment: A03
# Draw a piano in a room
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle
wn = turtle.Screen()
def start_t():
    #Defining turtles we are going to use
    turtle.bgcolor("blue")
    global black_k
    global white_k
    global tb
    global k
    global wn
    black_k = turtle.Turtle()
    white_k = turtle.Turtle()
    tb = turtle.Turtle()
    white_k.speed(10)

    #Adding attributes to the turtles
    white_k.color("purple","white")
    black_k.color("red","black")
    tb.color("black", "#8B4513") #color is brown in hex
    white_k.penup()
    white_k.goto(-200,50)
    white_k.left(90)
    k = 10 #size of keys on the piano



def Piano():
    """ Creating a piano without the keys """
    global k
    black_k.begin_fill()
    black_k.penup()
    black_k.goto((-60.00,100.00))
    black_k.pendown()
    for i in range(2):
        black_k.right(90)
        black_k.forward(60)
        black_k.right(90)
        black_k.forward(275)
    black_k.left(90)
    black_k.forward(50)
    black_k.left(90)
    black_k.forward(280)
    black_k.left(90)
    black_k.forward(50)
    black_k.left(90)
    black_k.forward(280)
    black_k.end_fill()

def Keys():
    """ Creating the white keys of the piano"""
    white_k.begin_fill()
    k = 10
    for i in range(25):
        for i in range(2):
            white_k.pendown()
            white_k.forward(50)
            white_k.right(90)
            white_k.forward(10)
            white_k.right(90)
        white_k.forward(50)
        white_k.right(90)
        white_k.forward(k)
        white_k.right(90)
        k = k + 10
    white_k.end_fill()
    print(white_k.position)

def table():
    """ making a table next to the piano """

    tb.begin_fill()
    tb.circle(50)
    tb.end_fill()
    for i in range(2):
        tb.begin_fill()
        if i < 1:
            tb.backward(10)
            tb.right(90)
            tb.forward(30)
            tb.left(90)
            tb.forward(10)
            tb.left(90)
            tb.forward(30)
        else:
            tb.right(90)
            tb.forward(10)
            tb.right(90)
            tb.forward(30)
            tb.left(90)
            tb.forward(10)
            tb.left(90)
            tb.forward(35)
            tb.left(90)
            tb.forward(20)
        tb.end_fill()

def main():
    """ main function enables all the previous definitions used"""
    start_t()
    table()
    Piano()
    Keys()

main()
wn.exitonclick()

