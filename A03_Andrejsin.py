
#############################################################################################
#David Andrejsin
#A03
#https://docs.google.com/document/d/1fjagvn8yhBAxHJrr9_yfCLMdc4kRXI6UZrAFnMdmwJw/edit?usp=sharing
#############################################################################################

import turtle
wn = turtle.Screen()
wn.bgcolor("Blue")
dave = turtle.Turtle()
wn.colormode(255)
dave.pencolor(31, 40, 132) #sets custom color for the pen

dave.speed(10)
def head():
    """Drawing head"""
    dave.penup()
    dave.setposition(0, 140)
    dave.pendown()
    dave.pensize(10)
    for i in range(12):
        dave.forward(25)
        dave.left(30)

def body():
    """Drawing Body"""
    dave.setposition(10,140)
    dave.right(90)
    dave.forward(200)

def legs():
    """Drawing legs"""
    dave.right(45)
    dave.forward(180)
    dave.setposition(10,-60)
    dave.left(90)
    dave.forward(180)

def arms():
    """Drawing arms"""
    dave.penup()
    dave.setposition(10,40)
    dave.pendown()
    dave.left(90)
    dave.forward(150)
    dave.setposition(10, 40)
    dave.left(90)
    dave.forward(150)

def hair():
    """Drawing brutal hairstyle"""
    dave.penup()
    dave.setposition(-20, 220)
    dave.pendown()
    dave.right(50)
    for i in range(3):
        dave.pencolor("Brown")
        dave.forward(30+10)
        dave.right(150)
        dave.forward(30+10)
        dave.left(150)

def main():
    """Calls all the functions"""
    head()
    body()
    legs()
    arms()
    hair()
    wn.exitonclick()




main() #calls the main function

# i finished coding here