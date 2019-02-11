######################################################################
# Author: Anna Heremes
# Username: heremesa
#
# Google Doc link - https://docs.google.com/document/d/1yCQfE_FiUNe92sQm6q4uFHCBj1JHMS-zqJ3MtALIzuc/edit?usp=sharing
# Assignment: A03: A Pair of fully Functional Gitty Psychedelic Robotic Turtles
######################################################################
# Acknowledgements:
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################


# importing the library that allows turtles to move in different directions
import random
import turtle

import turtle
turtle.bgcolor("blue")

wn = turtle.Screen()

import turtle

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")

side=20
myPen.penup()
myPen.goto(0,0) #position cursor at the bootom right of the screen
myPen.pendown()

for i in range (1,50):
  myPen.forward(side)
  myPen.left(92)
  side=side+7


myPen.penup()
myPen.goto(500,500)

#Start Spiral
#for i in range (1,20):
#  for j in range (0,4):
#      myPen.forward(side)
#      myPen.left(90)
#  myPen.left(20)
#  side=side+5


t0 = turtle.Turtle()
# creating the clones of the t0
t1 = t0.clone()
t2 = t0.clone()
t3 = t0.clone()
t4 = t0.clone()

for turtle in wn.turtles():
    turtle.penup()
    # this command hides the turtle so that the drawing process speeds up
    turtle.ht()

    # moving turtles randomly on the screen
    turtle.right(random.randrange(361))
    turtle.shape("turtle")

    # adapts the appearance of the turtle according to the values of outline
    turtle.resizemode("user")
    n = random.uniform(0.5,1)
    turtle.shapesize(n,n,n)
    # make the turtle visible
    turtle.st()

# if turtle gets caught by other turtle, it resets and starts appearing again
def caught(x,y):
    for turtle in wn.turtles():
        turtle.reset()
        turtle.penup()

while 1:

    for turtle in wn.turtles():
        turtle.forward(2)
        # return an random integer in the interval (-30,0)
        turtle.right(33 - random.randrange(63))
        # when the user clicks on the turtle, it triggers function caught and the turtles restart again
        turtle.onclick(caught)