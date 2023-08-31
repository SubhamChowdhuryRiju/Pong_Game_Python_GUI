from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounce_y()

    # Collision with Paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Miss by Right Paddles
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()

    # Miss by Left Paddles
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

    # Winning Logic
    # If left paddle scores 10 first
    if score.l_score == 10:
        is_game_on = False
        score.game_over("LEFT")

    # If right paddle scores 10 first
    if score.r_score == 10:
        is_game_on = False
        score.game_over("LEFT")

screen.exitonclick()
