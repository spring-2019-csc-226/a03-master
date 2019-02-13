#################################################################################
# Author: Karmadri Santiago
# Username: karmadri
##https://docs.google.com/document/d/1TRK3r3jXSy2-E-BIFyDExYeiwuXY0kS3Ib38PTBQ4Ho/edit?usp=sharing
# Assignment: A03 A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
import turtle
turtle.colormode(255)
turtle.bgcolor(0,37,107)

turtle.setup(800, 800)
wn = turtle.Screen()
hboy=turtle.Turtle()
hboy.penup()
hboy.pensize(10)
hboy.goto(-300, -300)
hboy.pendown()
hboy.forward(100)
hboy.left(75)
hboy.forward(250)
hboy.right(75)
hboy.forward(130)
hboy.right(75)
hboy.forward(250)
hboy.left(75)
hboy.forward(100)
hboy.left(87)
hboy.forward(550)
hboy.left(93)
hboy.forward(110)
hboy.left(75)
hboy.forward(280)
hboy.right(75)
hboy.forward(150)
hboy.right(75)
hboy.forward(280)
hboy.left(75)
hboy.forward(110)
hboy.left(93)
hboy.forward(550)
hboy.penup()
hboy.goto(-200,280)
hboy.write("Honda, The Power of Dreams", font=("Arial", 16, "italic"))


wn.exitonclick()