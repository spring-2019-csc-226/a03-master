# William Miller
# google doc: https://docs.google.com/document/d/1oCmkFmXKiNwrCovisisTkf_3qdvQ6QJMvHSO_5YftwM/edit#
import turtle


def make_circle(smiley):
    smiley.setpos(0,-200)
    smiley.circle(200)


def make_other_lines(smiley):
    smiley.left(90)
    smiley.forward(400)
    smiley.backward(200)
    smiley.right(45)
    smiley.forward(200)
    smiley.backward(200)
    smiley.left(90)
    smiley.forward(200)


def main():
    wn = turtle.Screen()
    wn.bgcolor("black")
    smiley = turtle.Turtle()
    smiley.color("white")
    smiley.pensize(10)
    smiley.shape("circle")

    make_circle(smiley)
    make_other_lines(smiley)
    wn.exitonclick()

main()










