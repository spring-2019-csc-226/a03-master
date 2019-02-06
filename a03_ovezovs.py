######################################################################
# Author: Shageldi Ovezov       TODO: Change this to your name, if modifying
# Username: ovezovs               TODO: Change this to your username, if modifying
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles

# Link to Google Doc: https://docs.google.com/document/d/1wgsvdjrb2tgBFyVABeXgK7uowny3nAHx5ePXOtTstNE/edit?usp=sharing

######################################################################

import turtle

# creating a screen
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(137, 188, 249)

# creating turtle #1 named greg
greg = turtle.Turtle()
greg.speed(6)
greg.hideturtle()

# creating turtle #2
luxa = turtle.Turtle()
luxa.color("yellow")
luxa.hideturtle()

# defining a function that would draw a teddy bear
def make_bear(sz, clr, sc):
    """draws a teddy bear with eyes. Eyes turn into sunglasses if the weather is sunny"""
    greg.color(clr)

    # drawing head
    greg.penup()
    greg.pendown()
    greg.begin_fill()
    greg.circle(sz)    # head circle
    greg.end_fill()
    # drawing two ears
    greg.penup()
    greg.left(90)
    greg.forward(sz*1.5)
    greg.right(90)
    greg.forward(sz)
    greg.pendown()
    greg.begin_fill()
    greg.circle(sz / 2.7)  # right ear
    greg.penup()
    greg.backward(2*sz)
    greg.pendown()
    greg.circle(sz/2.7)   # left ear
    greg.end_fill()
    greg.pos()
    # drawing main body
    greg.penup()
    greg.goto(0, 4)
    greg.pendown()
    greg.begin_fill()
    greg.circle(-sz*1.8)
    greg.end_fill()
    # drawing legs
    greg.penup()
    greg.begin_fill()
    greg.goto((sz*1.2), -(sz*3.1))
    greg.pendown()
    greg.circle(-(sz/2.2))   # right leg
    greg.penup()
    greg.backward(sz*2.4)
    greg.pendown()
    greg.circle(-(sz / 2.2))
    greg.end_fill()

    # draw sunglasses that will be used as eyes of the bear when there is no sun

    greg.pencolor("black")
    greg.fillcolor(42, 221, 209)
    greg.penup()
    greg.goto(0, 0)
    greg.left(90)
    greg.forward(sz*1.2)
    greg.right(90)
    greg.forward(sz/2.4)
    greg.pendown()
    greg.begin_fill()
    greg.circle(sz/4.3)   # right side
    greg.penup()
    greg.backward(sz/1.2)
    greg.pendown()
    greg.circle(sz / 4.3)   # left side
    greg.end_fill()

    # connecting eyes with a line in order to make sunglasses
    if sc == True:
        greg.pensize(4)
        greg.pencolor(42, 221, 209)
        greg.penup()
        greg.left(90)
        greg.forward(sz/4.3)
        greg.right(90)
        greg.pendown()
        greg.forward(sz/1.2)


def make_sun():
    """draws sun if the weather is sunny"""
    if sun_or_cloud is True:
        luxa.speed(8)
        luxa.penup()
        luxa.goto(230, 190)
        luxa.pendown()
        luxa.begin_fill()
        luxa.circle(40)
        luxa.end_fill()
    else:
        pass

# Allowing user to input the size and color of the bear and the condition of weather

bear_size = int(input("Choose your bear's size: "))
bear_color = input("Now choose color: ")

sun_or_cloud = input("What is the weather like [Sunny or Cloudy]: ").lower()
# checking if user chose sunny, cloudy or other condition of weather:
if sun_or_cloud == "sunny":
    sun_or_cloud = True
else:
    sun_or_cloud = False

def main():
    """creating the function in order to call all other functions inside of it"""

    make_bear(bear_size, bear_color, sun_or_cloud)
    make_sun()

main()

wn.exitonclick()