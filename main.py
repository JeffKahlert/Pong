from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score


def kill_game():
    global game_loop
    game_loop = False


screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
paddle_left = Paddle("left")
paddle_right = Paddle("right")
ball = Ball()
score = Score()

screen.onkey(key="Up", fun=paddle_left.move_up)
screen.onkey(key="Down", fun=paddle_left.move_down)

screen.onkey(key="w", fun=paddle_right.move_up)
screen.onkey(key="s", fun=paddle_right.move_down)

screen.onkey(key="q", fun=kill_game)

game_loop = True

while game_loop:
    screen.update()
    time.sleep(0.01)
    ball.ball_movement()
    if ball.xcor() > 780 or ball.xcor() < -780 or ball.ycor() > 240\
            or ball.ycor() < -240:
        ball.bounce('wall')

    if ball.distance(paddle_right) < 50 and ball.xcor() > 370\
            or ball.distance(paddle_left) < 50 and ball.xcor() < -370:
        ball.bounce('paddle')

    if ball.xcor() < -400 or ball.xcor() > 400:
        if ball.xcor() < -400:
            score.increase_score("right")
        else:
            score.increase_score("left")
        ball.restart_game()

screen.exitonclick()
