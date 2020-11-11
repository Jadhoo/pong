# pong game by @jadhoo

import turtle
import winsound
import time

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


# scores
score_a = 0
score_b = 0

# score board
score_board = turtle.Turtle()
score_board.color("white")
score_board.penup()
score_board.setposition(0, 260)
score_board.hideturtle()
score_board.write('Player 1: 0 | Player 2: 0', move=False, align='center', font=("Courier", 20, "normal"))

# initially the ball is in rest
move_ball = False

# brings the ball in motion
def release_ball():
    global move_ball
    move_ball = True

# reset the positions of ball and paddle when a player scores
def reset_positions():
    global move_ball
    move_ball = False
    ball.setposition(0, 0)
    paddle_a.setposition(-350, 0)
    paddle_b.setposition(350, 0)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(release_ball, "space")

while(True):
    wn.update()

    # move ball
    if move_ball:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

    # ball collission on top border
    if ball.ycor() > 290:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    # ball collission on bottom border
    if ball.ycor() < -290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    # when left paddle scores
    if ball.xcor() > 350:
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        score_a += 1
        score_board.clear()
        score_board.write("Player 1: {} | Player 2: {}".format(score_a, score_b), move = False, align = "center", font = ("Courier", 20, "normal"))
        time.sleep(1.5)
        reset_positions()
    
    # when right paddle scores
    if ball.xcor() < -350:
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        score_b += 1
        score_board.clear()
        score_board.write("Player 1: {} | Player 2: {}".format(score_a, score_b), move = False, align = "center", font = ("Courier", 20, "normal"))
        time.sleep(1.5)
        reset_positions()

    # ball collission with left paddle
    if ball.xcor() < -330 and (ball.ycor() > paddle_a.ycor() - 50 and ball.ycor() < paddle_a.ycor() + 50) :
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(-330)
        ball.dx *= -1

    # ball collission with right paddle
    if ball.xcor() > 330 and (ball.ycor() > paddle_b.ycor() - 50 and ball.ycor() < paddle_b.ycor() + 50) :
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(330)
        ball.dx *= -1 

