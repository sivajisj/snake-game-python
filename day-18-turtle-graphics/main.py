import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
# colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta", "teal", "lime"]

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

directions = [0, 90, 180, 270]
tim.width(9)
tim.speed("fastest")

for _ in range(200):
    tim.fd(25)
    tim.setheading(random.choice(directions))
    rndm_color = random_color()
    tim.color(rndm_color)













screen = Screen()
screen.exitonclick()