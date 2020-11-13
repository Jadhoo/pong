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
ball.dx = 0.5
ball.dy = 0.5
ball.hideturtle()

# functions for game controlls

# f1: move left paddle up
def paddle_a_up():
    y = paddle_a.ycor()
    if y <= 240 and game_status == 1:
        y += 20
        paddle_a.sety(y)

# f2: move left paddle down
def paddle_a_down():
    y = paddle_a.ycor()
    if y >= -220 and game_status == 1:
        y -= 20
        paddle_a.sety(y)

# f3: move right paddle up
def paddle_b_up():
    y = paddle_b.ycor()
    if y <= 240 and game_status == 1:
        y += 20
        paddle_b.sety(y)

# f4: move right paddle down
def paddle_b_down():
    y = paddle_b.ycor()
    if y >= -220 and game_status == 1:
        y -= 20
        paddle_b.sety(y)


# scores
score_a = 0
score_b = 0

# reset the score back to zero
def reset_score():
    global score_a, score_b
    score_a, score_b = 0, 0
    score_board.clear()
    score_board.write('Player 1: 0 | Player 2: 0', move=False, align='center', font=("Courier", 20, "normal"))

# score board
score_board = turtle.Turtle()
score_board.color("white")
score_board.penup()
score_board.setposition(0, 260)
score_board.hideturtle()
score_board.write('Player 1: 0 | Player 2: 0', move=False, align='center', font=("Courier", 20, "normal"))

# initially the ball is in rest
move_ball = False

# brings the ball in motion. here this function is called on pressing space button
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

# game status
# game_status = 1 => on game
# game_status = 2 => play or pause game
# game_status = 3 => game over

game_status = 1
winner = None

# game message
game_msg = turtle.Turtle()
game_msg.color("red")
game_msg.penup()
game_msg.hideturtle()
game_msg.setposition(0, 0)



# control to play or pause the game when "p" is pressed
def play_pause():
    global game_status
    if game_status == 1:
        game_status = 2
        ball.hideturtle()
    elif game_status == 2:
        game_status = 1
        ball.showturtle()
    elif game_status == 3:
        reset_positions()
        reset_score()
        ball.showturtle()
        game_status = 1

# to play game_over sound
game_over = False

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(release_ball, "space")
wn.onkey(play_pause, "p")

# game intro
game_msg.write("PONG", move = False, align = "center", font = ("Comic Sans MS", 40, "bold"))
game_msg.goto(0, game_msg.ycor() - 50)
game_msg.write("Press space to release the ball", align = "center", font = ("Helvetica", 20, "normal"))
time.sleep(2)
game_msg.clear()
ball.showturtle()

# main loop
while(True):
    wn.update()
    # game in progress
    if game_status == 1:
        game_msg.clear()
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
        elif ball.ycor() < -290:
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            ball.sety(-290)
            ball.dy *= -1

        # when left paddle scores
        if ball.xcor() > 350:
            score_a += 1
            if score_a < 2:
                winsound.PlaySound("score.wav", winsound.SND_ASYNC)
            else:
                winner = "Player 1"
                game_status = 3
                game_over = True
            score_board.clear()
            score_board.write("Player 1: {} | Player 2: {}".format(score_a, score_b), move = False, align = "center", font = ("Courier", 20, "normal"))
            time.sleep(1.5)
            reset_positions()
        
        # when right paddle scores
        elif ball.xcor() < -350:
            score_b += 1
            if score_b < 2:
                winsound.PlaySound("score.wav", winsound.SND_ASYNC)
            else:
                winner = "Player 2"
                game_status = 3
                game_over = True
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
        elif ball.xcor() > 330 and (ball.ycor() > paddle_b.ycor() - 50 and ball.ycor() < paddle_b.ycor() + 50) :
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            ball.setx(330)
            ball.dx *= -1 
    
    # game is paused
    elif game_status == 2:
        game_msg.write("Game Paused! press p to resume", move = False, align = "center", font = ("Comic Sans MS", 30, "bold italic"))

    # game over
    else:
        if game_over:
            winsound.PlaySound("game_over.wav", winsound.SND_ASYNC)
            game_over = False
        game_msg.clear()
        game_msg.setposition(0, 0)
        ball.hideturtle()
        game_msg.write("{:^50}\n{:^50}".format((winner +  " wins🥳"), "Press p to play again"), move = False, align = "center", font = ("Comic Sans MS", 30, "bold"))