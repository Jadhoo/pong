# pong game by @jadhoo

import turtle

# initial setup
wn = turtle.Screen()
wn.title("Pong game by Jadhoo")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(10)

while(True):
    wn.update()