# pong game by @jadhoo

import turtle

# initial setup
wn = turtle.Screen()
wn.title("Pong game by Jadhoo")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(10)

# left paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.setposition(-350, 0)
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)

# right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.setposition(350, 0)
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)

while(True):
    wn.update()