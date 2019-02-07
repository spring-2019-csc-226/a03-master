import turtle

def draw_roof(wn, turt_draw):
    turt_draw.pendown()
    turt_draw.color("Red")
    turt_draw.begin_fill()

    for i in range(4):
        turt_draw.forward(200)
        turt_draw.left(90)
    turt_draw.left(90)

    turt_draw.end_fill()

    turt_draw.forward(200)

    turt_draw.begin_fill()
    for i in range(2):
        turt_draw.right(60)
        turt_draw.forward(115)

    turt_draw.end_fill()
    turt_draw.penup()


def draw_color(turt_draw):
    """
    Draws my house
    :param turt_draw:
    :return:
    """
    turt_draw.left(90)
    turt_draw.forward(400)




def draw_door(turt_draw):
    """
    Draws my door
    :param turt_draw:
    :return:
    """
    pass

def draw_enviroment(turt_draw):
    """
    Draws my wacky landscape
    :param turt_draw:
    :return:
    """
    turt_draw.pensize(5)
    turt_draw.pendown()
    turt_draw.pencolor("green")
    turt_draw.beginfill()
    turt_draw.setposition(0,0)
    turt_draw.forward(500)
()
def main():
    """
    Draws my house with my detailed landscape

    :return:
    """

    wn = turtle.Screen()
    turt_draw = turtle.Turtle()
    turt_draw.hideturtle()
    draw_roof(wn,turt_draw)
    draw_color(turt_draw)
    wn.bgcolor("blue")



    wn.exitonclick()


main()  # Calls main()
