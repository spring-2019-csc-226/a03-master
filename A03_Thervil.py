import turtle
wn = turtle.Screen()
wn.bgcolor("black")

willy = turtle.Turtle()
willy.shape('turtle')
willy.setheading(90)
willy.setpos(0, 0)

jess = turtle

def function_1():
    """ creates shape
        :param : turtle object"""
    willy.color('green')
    willy.begin_fill()
    for t in range(9):
        willy.forward(90)
        willy.left(45)
    willy.end_fill()
    willy.hideturtle()

jess.setpos (-145, -65)
jess.pendown()

def function_2():
    """creates tree log
    :param : turtle object"""
    jess.color("brown")
    jess.begin_fill()
    for t in range(2):
        jess.forward(75)
        jess.right(90)
        jess.forward(150)
        jess.right(90)
    jess.end_fill()
    jess.hideturtle()


def function_3():
    """creates house
    :param : turtle object"""
    jess.color("blue")
    jess.pensize(5)
    jess.penup()
    jess.setpos(80, -215)
    jess.pendown()
    for j in range(4):
        jess.forward(150)
        jess.left(90)

def function_4():
    """creates house
    :param : turtle object"""
    jess.color("red")
    jess.pensize(5)
    jess.penup()
    jess.setpos(80, -65)
    jess.pendown()
    for j in range(1):
        jess.forward(150)
        jess.left(145)
        jess.forward(90)
        jess.left(70)
        jess.forward(90)

def function_5():
    """ creates star
        :param : turtle object"""
    willy.color("sky blue")
    willy.pensize(1)
    willy.penup()
    willy.setpos(250, 100)
    willy.pendown()
    willy.begin_fill()
    for t in range(5):
        willy.forward(90)
        willy.left(145)
    willy.end_fill()
    willy.hideturtle()

def main():
    function_1()
    function_2()
    function_3()
    function_4()
    function_5()

    wn.exitonclick()
#coment coment
# Turtle

main()                          # calls the main function
