from turtle import Screen
from paddle import Paddle
from ball import Ball
from edges import Edge_1, Edge_2
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)


paddle_1 = Paddle((-390, 0))
paddle_2 = Paddle((383, 0))

ball = Ball()
edge_1 = Edge_1((0, -298))
edge_2 = Edge_2((0, 304))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_2.go_up, "Up")
screen.onkey(paddle_2.go_down, "Down")
screen.onkey(paddle_1.go_up, "w")
screen.onkey(paddle_1.go_down, "s")


is_on = True
while is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() > 279 or ball.ycor() < -276:
        ball.bounce_y()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 350 or ball.distance(paddle_1) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()