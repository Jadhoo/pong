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

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.setposition(0, 0)
ball.penup()
ball.dx = 0.3
ball.dy = 0.3

# functions

# f1: move left paddle up
def paddle_a_up():
    y = paddle_a.ycor()
    if y <= 240:
        y += 20
        paddle_a.sety(y)

# f2: move left paddle down
def paddle_a_down():
    y = paddle_a.ycor()
    if y >= -220:
        y -= 20
        paddle_a.sety(y)

# f3: move right paddle up
def paddle_b_up():
    y = paddle_b.ycor()
    if y <= 240:
        y += 20
        paddle_b.sety(y)

# f4: move right paddle down
def paddle_b_down():
    y = paddle_b.ycor()
    if y >= -220:
        y -= 20
        paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while(True):
    wn.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball collission on top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # ball collission on bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # ball collission with left paddle
    if ball.xcor() < -330 and (ball.ycor() > paddle_a.ycor() - 50 and ball.ycor() < paddle_a.ycor() + 50) :
            ball.setx(-330)
            ball.dx *= -1

    # ball collission with right paddle
    if ball.xcor() > 330 and (ball.ycor() > paddle_b.ycor() - 50 and ball.ycor() < paddle_b.ycor() + 50) :
            ball.setx(330)
            ball.dx *= -1 

