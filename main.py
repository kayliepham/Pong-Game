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

screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
# if player uses key "w" or "s", move (not case-sensitive)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
screen.onkey(key="W", fun=l_paddle.move_up)
screen.onkey(key="S", fun=l_paddle.move_down)


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 282 or ball.ycor() < -282:
        ball.bounce_wall()

    # detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        ball.move_speed *= 0.9


    # detect when r_paddle misses; ball out of bounds
    # ball goes to l_paddle
    if ball.xcor() > 380:
        ball.reset_position(225)
        scoreboard.l_point()
        ball.move_speed *= 0.9

    # detect when l_paddle misses; ball out of bounds
    # ball goes to r_paddle
    if ball.xcor() < -380:
        ball.reset_position(45)
        scoreboard.r_point()
        ball.move_speed = 0.1





screen.exitonclick()
