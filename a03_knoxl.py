#Name: Lesley Knox
#DocLink: https://docs.google.com/document/d/1ltF6mcxAnhTkeWUuYL-xHovc4YBYW01G1-KWuhrZq3g/edit?usp=sharing

import turtle

def main():

    wn = turtle.Screen()
    wn.bgcolor("sky blue")

    tim = turtle.Turtle()
    tim.pen()
    tim.pensize(2)
    tim.shape("circle")
    tim.speed(3)


    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)

    # Position for roof
    tim.right(90)

    # Make a roof
    tim.forward(100)
    tim.right(-120)
    tim.forward(100)
    tim.right(-120)
    tim.forward(100)
    tim.right(-120)

    tim2 = turtle.Turtle()

    tim2.pen()
    tim2.pensize(2)
    tim2.shape("circle")
    tim2.penup()
    tim2.goto(-200, 0)
    tim2.showturtle()
    tim2.speed(3)

    tim2.pendown()

    tim2.forward(100)
    tim2.right(90)
    tim2.forward(100)
    tim2.right(90)
    tim2.forward(100)
    tim2.right(90)
    tim2.forward(100)

    # Position for roof
    tim2.right(90)

    # Make a roof
    tim2.forward(100)
    tim2.right(-120)
    tim2.forward(100)
    tim2.right(-120)
    tim2.forward(100)
    tim2.right(-120)

    tim2.penup()

    tim2.goto(250, -100)
    tim2.left(80)
    tim2.forward(350)

    tim2.pendown()
    #draw sun
    tim2.begin_fill()
    tim2.color("yellow")
    for x in range(20):
        tim2.left(90)
        tim2.forward(50)
        tim2.right(5)
    tim2.end_fill()

    tim.penup()
    tim.forward(20)
    tim.right(90)
    tim.forward(45)

    tim.pendown()
    #make double doors for house
    tim.left(90)
    tim.forward(55)
    tim.right(90)
    tim.forward(55)
    tim.right(90)
    tim.forward(27.5)
    tim.right(90)
    tim.forward(55)
    tim.left(90)
    tim.forward(27.5)
    tim.left(90)
    tim.forward(55)

    tim.penup()
    tim.right(90)
    tim.forward(157)

    tim.pendown()
    #make door for house
    tim.right(90)
    tim.forward(55)
    tim.left(90)
    tim.forward(27.5)
    tim.left(90)
    tim.forward(55)

    tim2.penup()
    tim2.right(70)
    tim2.forward(400)

    #draw grass
    tim2.color("green")
    tim2.right(90)
    tim2.pendown()
    tim2.pensize(50)
    tim2.forward(600)
    tim2.right(90)
    tim2.forward(30)
    tim2.right(90)
    tim2.forward(600)
    tim2.right(90)
    tim2.forward(-30)
    tim2.right(90)
    tim2.forward(600)
    tim2.right(30)


    wn.exitonclick()

main()