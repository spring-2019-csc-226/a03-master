#################################################################################
# Author: Roberto Santos
# Username: Santosr
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic  Robotic Turtles
# Purpose: Learning how to define and call functions.
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

wn = turtle.Screen()
wn.bgcolor("blue")

jose = turtle.Turtle()        # Making jose to make the body of the truck
jose.color("grey")
jose.hideturtle()
jose.speed(0)

martin = turtle.Turtle()      # Making martin to make the tires of the truck and the window
martin.color("black")
martin.hideturtle()
martin.speed(0)

eric = turtle.Turtle()        # Making eric to make the tires of the truck
eric.color("black")
eric.hideturtle()
eric.speed(0)

jacob = turtle.Turtle()       # Making jacob to make the building that the truck will be backing up into
jacob.color("black", "brown")
jacob.speed(0)

james = turtle.Turtle()       # Making james to make the windows of the building
james.color("black")
james.speed(0)

martha = turtle.Turtle()      # Making martha to make the road
martha.color("yellow")

cord_of_wind = [(-260, 190), (-220, 170), (-160, 170), (-120, 190), (-100, 190), (-260, 110), (-200, 110), (-160, 130), (-140, 130), (-100, 110), (-240, 50), (-200, 70), (-180, 70), (-140, 50), (-80, 50)]


def make_windows():               # makes the windows of the building
    """ This function creates the windows of the building"""
    for i in range(15):
        james.penup()
        james.goto(cord_of_wind[i])
        james.pendown()
        james.forward(20)
        james.right(90)
        james.forward(20)
        james.right(90)
        james.forward(20)
        james.right(90)
        james.forward(20)


def make_building ():
    """ This function makes the building on the left side of the screen"""
    jacob.penup()
    jacob.goto(-70,-90)
    jacob.pendown()
    jacob.begin_fill()
    for i in range(2):         # This makes the outline of the building
        jacob.left(90)
        jacob.forward(300)
        jacob.left(45)
        jacob.forward(100)
        jacob.left(45)
        jacob.forward(200)
    jacob.end_fill()
    for i in range(2):
        jacob.left(90)
        jacob.forward(300)
        jacob.left(90)
        jacob.forward(200)
    make_windows()


def make_head_of_truck():    # This function makes the head of the truck
    """ This function makes the head of the truck and makes it look 3-D """
    martin.penup()
    martin.forward(310)
    martin.pendown()
    martin.begin_fill()
    martin.left(90)
    martin.forward(50)
    martin.left(45)
    martin.forward(70.710)
    martin.left(45)
    martin.forward(50)
    martin.left(90)
    martin.forward(100)
    martin.end_fill()
    martin.right(135)
    martin.forward(50)
    martin.right(45)
    martin.forward(100)
    martin.right(90)
    martin.forward(50)
    martin.right(45)
    martin.forward(50)


coordinates = [(20, -40), (60, -40), (140, -40), (180, -40), (290, -40)] # This variable sets the cordinates where I want the tires to be at


def make_tires ():            # This definition makes the tires of the truck
    """ This function makes the 5 tires of the truck"""
    for i in range(5):
        eric.penup()
        eric.goto(coordinates[i])
        eric.pendown()
        eric.begin_fill()
        eric.circle(20)
        eric.end_fill()


def make_truck():             # This function creates the truck
    """ This function makes the whole truck """
    make_head_of_truck()
    jose.begin_fill()         # This for loop has
    for i in range(2):
        jose.forward(200)
        jose.left(90)
        jose.forward(100)
        jose.left(90)
    jose.end_fill()
    jose.left(135)
    jose.forward(50)
    jose.right(45)
    jose.forward(100)
    jose.right(90)
    jose.forward(200)
    jose.right(45)
    jose.forward(50)
    make_tires()


tire_places = [(-350, -250), (-350, -200)]

middle_lines = [(-350, -190), (-270, -190), (-190, -190), (-110, -190), (-30, -190), (50, -190), (130, -190), (210, -190), (290, -190)]  # These are the coordinates where the lines of the road will be at


def make_road():
    """ This function makes the road"""
    martha.penup()
    martha.goto(-350, -250)
    martha.pendown()
    martha.begin_fill()
    martha.forward(700)
    martha.left(90)
    martha.forward(10)
    martha.left(90)
    martha.forward(700)
    martha.left(90)
    martha.forward(10)
    martha.end_fill()
    martha.penup()
    martha.goto(-350, -150)
    martha.left(90)
    martha.pendown()
    martha.begin_fill()
    martha.forward(700)
    martha.left(90)
    martha.forward(10)
    martha.left(90)
    martha.forward(700)
    martha.left(90)
    martha.forward(10)
    martha.end_fill()
    for i in range(9):
        martha.setheading(0)
        martha.penup()
        martha.goto(middle_lines[i])
        martha.pendown()
        martha.forward(50)
        martha.right(90)
        martha.forward(10)
        martha.right(90)
        martha.forward(50)
        martha.right(90)
        martha.forward(10)


def main():
    """ This is the main function where all my definitions are called"""
    make_truck()
    make_building()
    make_road()


main()
    
wn.mainloop()