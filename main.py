import time
from turtle import Turtle, Screen
from pong_ball import Ball

from pong import Pong

from paddle import Paddle

from score import Score

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")

screen.tracer(0)

ball = Ball()

ping = Pong()

ball.create()
ball.create_dash()

ping.create_pong()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

score = Score()

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


screen.onkey(l_paddle.up, "+")
screen.onkey(l_paddle.down, "-")


pong_on = True
while pong_on:
    screen.update()
    time.sleep(0.1)
    ping.create_pong()
    # Detect collision with wall.
    if ping.ycor() > 280 or ping.ycor() < -280:
        ping.collision_up()
    # Detect collision with paddle
    if ping.distance(r_paddle) < 50 and ping.xcor() > 320 or ping.distance(l_paddle) < 50 and ping.xcor() < -320:
        ping.collision_paddle()


    #
    if ping.xcor() > 380:
        ping.refresh()
        score.left_score()
    if ping.xcor() < -380:
        ping.refresh()
        score.right_score()


screen.exitonclick()