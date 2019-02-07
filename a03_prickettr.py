#################################################################################
# Author: Robert Prickett
# Username: prickettr
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic  Robotic Turtles
# Link: https://docs.google.com/document/d/1gMddsifPMImntv5zzTSnBIvh6N03kJfG7NIatMYG7ok/edit#
# Purpose: Learning how to define and call functions.
#################################################################################
# Acknowledgements:
# Black Sabbath
#
#################################################################################

import turtle


def title_1(ozzy):
    """
    This function draws the words Black Sabbath in purple
    :return:

    """
    ozzy.color("purple")
    ozzy.hideturtle()
    ozzy.penup()
    ozzy.setposition(-25,190)
    ozzy.pendown()

    ozzy.write("BLACK", move=False, align='center', font=('Letraset', 75, ('italic', 'normal')))
    ozzy.penup()


    ozzy.setposition(-50,75)
    ozzy.pendown()
    ozzy.write("SABBATH", move=False, align='center', font=('Letraset', 110, ('italic', 'normal')))
    ozzy.penup()

def title_2(ozzy):
    """
    This function draws the words Masters Of Reality in #A1A1A1 color
    :return:
    """

    ozzy.color("#A1A1A1")

    ozzy.penup()
    ozzy.setposition(-20,-30)
    ozzy.pendown()
    ozzy.write("MASTER", move=False, align='center', font=('Letraset', 110, ('italic', 'normal')))
    ozzy.penup()

    ozzy.setposition(-60,-140)
    ozzy.pendown()
    ozzy.write("OF", move=False, align='center', font=('Letraset', 110, ('bold', 'normal')))
    ozzy.penup()

    ozzy.setposition(-55,-260)
    ozzy.pendown()
    ozzy.write("REALITY", move=False, align='center', font=('Letraset', 110, ('italic', 'normal')))
    ozzy.penup()


def title_embelish(ozzy):
    """
    This function draws some emblishments to make the album cover look somewhat authentic.
    :return:
    """
    ozzy.setposition(-107,-90)
    ozzy.color("#A1A1A1")
    ozzy.pensize(40)
    ozzy.pendown()

    ozzy.begin_fill()

    for i in range(8):
        ozzy.left(45)
        ozzy.forward(30)




def main():
    """
    This is the main function for drawing Masters Of Reality

    :return:
    """
    wn = turtle.Screen()
    wn.bgcolor("black")
    ozzy = turtle.Turtle()



    title_1(ozzy)
    title_2(ozzy)
    title_embelish(ozzy)

    wn.exitonclick()
main()

