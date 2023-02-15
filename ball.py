import random
from turtle import Turtle
import random

random_start_dir = [-1, 1]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.start_xpos = 0
        self.start_ypos = 0
        self.start_game()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5)
        self.speed("fastest")
        self.penup()
        self.x_move = 3
        self.y_move = 3

    def ball_movement(self):
        new_ypos = self.ycor() + self.y_move
        new_xpos = self.xcor() + self.x_move
        self.goto(new_xpos, new_ypos)

    def start_game(self):
        x_pos = random.choice(random_start_dir)
        y_pos = random.choice(random_start_dir)
        new_x_cor = self.xcor() + x_pos
        new_y_cor = self.ycor() + y_pos
        self.goto(new_x_cor, new_y_cor)

    def bounce(self, obj):
        if obj == 'wall':
            self.y_move *= -1
        if obj == 'paddle':
            self.x_move *= -1

    def restart_game(self):
        self.setx(self.start_xpos)
        self.sety(self.start_ypos)
        self.x_move *= -1
        self.start_game()