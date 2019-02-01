########################################################################################################################
# Dustin Cooper
# Google Link: https://docs.google.com/document/d/13b-mO7hPkeeyymAXIvNKipsWfx7bjD35LPHF6dhl3TU/edit#
#
# Purpose: Create a complex shape such as a house
########################################################################################################################

import turtle

def draw_house(t, sz):
   t.penup()
   t.backward(200)
   t.right(90)
   t.forward(250)
   t.left(180)
   t.pendown()
   """
   This function creates the walls of my house along with the roof
   """
   for i in range(4):              #creates the walls of house
       t.color("black")
       t.forward(sz)
       t.right(90)
   t.forward(sz)                   #creates roof of house
   t.right(45)
   t.forward(212)
   t.right(90)
   t.forward(212)

def draw_window(n, wl, bk):         #draws a window
   n.penup()
   n.backward(bk)                  #sets position of window
   n.pendown()
   for i in range(4):              #creates outside box of window
       n.color("#FFFFFF")
       n.forward(wl)
       n.right(90)
   n.forward(25)
   n.right(90)
   n.forward(wl)
   for i in range(2):              #creates the crossbeams inside window
       n.right(90)
       n.forward(25)
   n.right(90)
   n.forward(wl)
   n.left(90)
   n.forward(25)
   n.right(90)
   n.backward(wl)



   pass
def draw_door(d, ln):               #function that draws a door along with door handle
   d.penup()
   d.backward(75)
   d.right(90)
   d.forward(250)
   d.right(180)
   d.pendown()
   d.forward(ln)
   d.right(90)
   d.forward(50)
   d.right(90)
   d.forward(ln)
   d.penup()
   d.backward(50)
   d.left(90)
   d.backward(10)
   d.shape("circle")               #this code along with the next two lines creates the doorhandle
   d.turtlesize(0.5)
   d.stamp()

def draw_person(p):                 #very confusing code that creates a person
   p.penup()
   p.forward(200)
   p.right(90)
   p.forward(250)
   p.right(90)
   p.forward(50)
   p.pendown()
   p.backward(10)
   p.left(45)
   p.backward(30)
   p.left(90)
   p.forward(30)
   p.left(45)
   p.forward(10)
   p.backward(10)
   p.right(45)
   p.backward(30)
   p.right(45)
   p.backward(30)
   p.left(45)
   p.forward(30)
   p.backward(30)
   p.right(90)
   p.forward(30)
   p.backward(30)
   p.left(45)
   p.backward(20)
   p.turtlesize(1.4)
   p.shape("circle")
   p.stamp()

   pass

def main():
   """
   This main defenition sets up the window, turtles, and calls all other funtions
   """
   wn = turtle.Screen()
   wn.bgcolor("#21D4D4")
   house = turtle.Turtle()
   house.pensize(10)
   window = turtle.Turtle()
   window.color('wheat')
   window.pensize(10)
   door = turtle.Turtle()
   door.pensize(10)
   door.color("#000000")
   person = turtle.Turtle()
   person.pensize(5)
   person.color("#000000")
   # ...
   draw_house(house, 300)            # draws the outside box of my house along with the roof
   draw_window(window, 50, 0)
   draw_window(window, 50, 150)      # draws the window behind the original one
   draw_door(door, 100)              #draw a door
   draw_person(person)               #draws the person(couldnt figure out how to draw face)
   wn.exitonclick()

main()                                #executes the main funtion