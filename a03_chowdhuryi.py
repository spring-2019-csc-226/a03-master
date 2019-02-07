# Drawing constellations
import turtle

pen = turtle.Turtle()
pen.speed(0)
wn = turtle.Screen()
wn.bgcolor("#000777")
pen.color("#FFFFFF")


def constellation(constellation):
    # draw the first star
    pen.penup()
    pen.goto(constellation[0])
    pen.begin_fill()
    pen.circle(2)
    pen.end_fill()
    pen.pendown()
    # draw each line and star within the constellation
    for star in constellation:
        pen.goto(star)
        pen.begin_fill()
        pen.circle(2)
        pen.end_fill()
    # hide the turtle
    pen.penup()
    pen.goto(600, 600)

    # Coordinates of the constellations


plough = [[-140, 20], [-60, 25], [0, 10], [35, -5], [45, -50], [120, -60], [150, -5]]
cassiopeia = [[-90, 70], [-50, -10], [0, 0], [40, -50], [100, 0]]
leo = [[10, 30], [50, 10], [60, -40], [-90, -50], [-180, -70], [-110, 0], [10, 30], [15, 80], [60, 130], [80, 120]]

constellation(plough)
constellation(cassiopeia)
constellation(leo)
