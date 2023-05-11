from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

p1_paddle = Paddle(-350, 0)
p2_paddle = Paddle(350, 0)
ball = Ball()
screen.listen()

screen.onkey(p1_paddle.move_up, "w")
screen.onkey(p1_paddle.move_down, "s")
screen.onkey(p2_paddle.move_up, "Up")
screen.onkey(p2_paddle.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce("y")
    if ball.distance(p2_paddle.pos()) <= 50 and 320 < ball.xcor() < 350:
        ball.bounce("x")
    if ball.distance(p1_paddle.pos()) <= 50 and -320 > ball.xcor() > -350:
        ball.bounce("x")
        ball.bounce("y")
    # Scoring
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        if ball.xcor() >= 380:
            scoreboard.p2_point()
            scoreboard.update_scoreboard()
        elif ball.xcor() <= -380:
            scoreboard.p1_point()
            scoreboard.update_scoreboard()
        ball.setpos(0, 0)
        ball.move_speed = 0.1
        ball.bounce("x")



screen.exitonclick()