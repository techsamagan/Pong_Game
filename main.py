from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()
       
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()
     
screen.exitonclick()