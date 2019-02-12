import turtle
wn = turtle.Screen()
wn.bgcolor("black")

willy = turtle.Turtle()
willy.shape('turtle')
willy.setheading(90)
willy.setpos(0, 0)

jess = turtle
tess = turtle
tess.setpos(100, -200)
tess.pendown()

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
    jess.penup()
    jess.setpos(100, -250)
    jess.pendown()
    for j in range(4):
        pass


def main():
    function_1()
    function_2()
    function_3()

    wn.exitonclick()
#coment coment
# Turtle

main()                          # calls the main function
