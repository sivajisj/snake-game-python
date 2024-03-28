from turtle import Turtle,Screen

otis = Turtle()

otis.width(1)
otis.speed("fastest")

otis.shape("turtle")

for _ in range(61):
    otis.circle(100)
    otis.left(6)


screen = Screen()
screen.exitonclick()
