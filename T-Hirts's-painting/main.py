from turtle import Screen
import random
import turtle as trtl

t = trtl.Turtle()
trtl.colormode(255)
t.speed(10000)


def random_color():
    """Generates random color with changed RGB values"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def nft_creator():
    """Generates random pictures (Inspired by Damien Hirst's paintings)"""
    degrees = (0, 90, 180, 270)

    # Sets Line thickness
    t.width(15)

    # Sets object speed
    t.speed(10)

    # Creates NTF object
    for _ in range(500):
        t.color(random_color())
        t.forward(30)
        t.setheading(random.choice(degrees))


screen = Screen()

nft_creator()

screen.exitonclick()
