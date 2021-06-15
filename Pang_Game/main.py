from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreborad import Score
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.down, "Down")
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.down, "s")
screen.onkey(l_paddle.up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart_position()
        score.increse_l()

    if ball.xcor() < -380:
        ball.restart_position()
        score.increse_r()

screen.exitonclick()