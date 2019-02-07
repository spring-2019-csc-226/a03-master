######################################################################################################
#Author's name: Kabelo Makotoko
#Username: makotokok
#Homework: A03- A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
#Purpose: Practice creating and using Functions, use turtle library more and learn more about source control and git.

#######################################################################################################

import turtle                                  # allows us to use the turtles libray


wn = turtle.Screen()
wn.bgcolor("brown")
kb = turtle. Turtle()
kb.color("black")
kb.pensize(10)

tumi = turtle.Turtle()
tumi.color("yellow")
tumi.pensize(10)

def draw_tilted_tube(kb):
   """
   makes a square shaped house
   """

   kb.setpos(50, 50)
   kb.speed(0)

   kb.begin_fill()
   for side in range(2):
      kb.forward(150)
      kb.left(90)
      kb.forward(150)
      kb.left(90)
      kb.forward(90)

      kb.end_fill()
def write_text(tumi):
    """"
    Writes a text in sotho language.
    """
    tumi.pu()
    tumi.setpos(-120, 150)
    tumi.pd()
    tumi.write("LUMELA AUSI")
    tumi.hideturtle()

def main():
    draw_tilted_tube(kb)
    write_text(tumi)


main()                                #allows us to call main function
wn.exitonclick()