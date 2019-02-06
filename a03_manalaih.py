######################################################################
# Author: Hila Manalai
# Username: manalaih
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To use turtle library, learn about color representation in computer, source code and git.
######################################################################
# Acknowledgements:

#
# A03 - Google Document link: https://docs.google.com/document/d/1B9F5a8D7kr8s4Z8O42pObc-YndtRh0frD6Mf7W5kJ2A/edit?usp=sharing
# first modified by Hila Manalai

######################################################################

# Make mountains, star and moon

import turtle

wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor("lightblue")

# First turtle draws the sun
sun = turtle.Turtle()
sun.hideturtle()
sun.penup()
sun.shapesize(8)
sun.goto(-90, 150)
sun.pendown()

sun.color("orange", "yellow")
sun.begin_fill()

for i in range(50):
    sun.speed(0)
    sun.forward(200)
    sun.left(170)

sun.end_fill()

# Second turtle draws mountain
mountain = turtle.Turtle()
mountain.hideturtle()
mountain.speed(0)
mountain.penup()
mountain.pensize(2)
mountain.goto(-350, -250)
mountain.pendown()
mountain.pencolor((51, 26, 0))

# Third turtle draws a cloud
cloud = turtle.Turtle()
cloud.hideturtle()
cloud.speed(0)
cloud.penup()
cloud.goto(90, 0)
cloud.pendown()


# Fourth turtle also draws a cloud
cloud_2 = turtle.Turtle()
cloud_2.hideturtle()
cloud_2.speed(0)
cloud_2.penup()
cloud_2.goto(-120, 100)
cloud_2.pendown()


# Fifth turtle draws the grass
grass = turtle.Turtle()
grass.hideturtle()
grass.speed(0)
grass.color("green")
grass.pensize(30)
grass.penup()
grass.goto(-350, -260)
grass.pendown()
grass.forward(670)

# Sixth turtle draws a tree
tree = turtle.Turtle()
tree.hideturtle()
tree.speed(0)
tree.pensize(10)
tree.penup()
tree.goto(200, -250)
tree.pendown()

# Seventh turtle draws a second tree
tree_2 = turtle.Turtle()
tree_2.hideturtle()
tree_2.speed(0)
tree_2.pensize(10)
tree_2.penup()
tree_2.goto(90, -250)
tree_2.pendown()


def draw_tree(t, h, r):
    """
    Draws a tree shape.
    """
    t.left(90)
    t.color((102, 53, 0))
    t.begin_fill()
    t.forward(h)
    t.end_fill()
    t.right(90)
    t.forward(r//10)
    t.color("green")
    t.begin_fill()
    t.circle(r, 360)
    t.end_fill()


def draw_could(c):
    """
    Draws cloud shape
    """

    c.color("white")
    c.fillcolor((255, 255, 255))
    c.begin_fill()
    c.forward(40)
    c.left(90)
    c.forward(10)
    c.circle(30, 180)
    c.right(180)
    c.circle(60, 180)
    c.forward(10)
    c.left(90)
    c.forward(150)
    c.end_fill()


def draw_mountain(m, h):
    """
    Draws mountains
    """
    m.fillcolor((51, 26, 0))
    m.begin_fill()
    for i in range(2):
        m.seth(65)
        m.forward(h)
        m.seth(-65)
        m.forward(h)

    m.end_fill()
    pass
    # ... pass: don't do anything with this function and just pass


def main():
    """
    Call to other functions
    """
    # ...
    draw_mountain(mountain, 400)            # Function call to draw_mountain function
    draw_could(cloud)                       # Function call to draw_cloud function
    draw_could(cloud_2)                     # Function call to draw_cloud to add a new cloud shape.
    draw_tree(tree, 40, 30)                 # Function call to draw_tree
    draw_tree(tree_2, 30, 30)               # Function call to draw_tree to add a new tree shape.
main()

wn.exitonclick()
