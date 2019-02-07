#################################################################################
# Authors: Azariah Mawoko
# Usernames: mawokoa
#
#
# Assignment: A3: Assignment: A3: A Pair of Fully Functional
#                  Gitty Psychedelic Robotic Turtles
# Credits:

import turtle


def draw_evilshroom():
    """
    Draws a the evil mushroom tree in turtle land
    :return:
    """
    shroom = turtle.Turtle()
    shroom.pensize(3)                          # Draws the top of the mushroom using loops.
    shroom.pencolor("green")
    shroom.penup()
    shroom.goto(-200, -190)
    shroom.pendown()
    shroom.fillcolor("green")
    shroom.begin_fill()
    for i in range(2):
        shroom.forward(30)
        shroom.left(90)
        shroom.forward(60)
        shroom.left(90)
    shroom.end_fill()
    shroom.pencolor("red")                          # Draws the trunk of the mushroom using loops.
    shroom.penup()
    shroom.goto(-200, -120)
    shroom.pendown()
    shroom.fillcolor("red")
    shroom.begin_fill()
    shroom.forward(30)
    shroom.right(45)
    shroom.circle(15, 200)
    for i in range(7):
        shroom.right(130)
        shroom.circle(15, 180)
    shroom.end_fill()


def turtle_attack(wn):
    """
    Makes Tino and causes him to spit fire to
    destroy the evil mushroom tree
    :return:

    """

    tino = turtle.Turtle()
    tino.color('silver')
    tino.penup()
    tino.shape('turtle')
    tino.setpos(200, 60)
    tino.right(160)
    for i in range(18):
        tino.stamp()
        tino.forward(20)
        wn.register_shape("fire1.gif")
        tino.shape("fire1.gif")


def main():                                  # Calls all the functions to run code.

    wn = turtle.Screen()
    wn.bgpic('Storm.gif')
    wn.bgcolor('Indigo')
    wn.title("Turtles Spit Fire!!")
    wn = turtle.Screen()
    draw_evilshroom()
    turtle_attack(wn)

    wn.exitonclick()


main()

