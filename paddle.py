from turtle import Turtle

UP = 90


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.side = side
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if self.side == 'left':
            self.goto(-380, 0)
        if self.side == 'right':
            self.goto(380, 0)

    def move_up(self):
        new_ypos = self.ycor() + 20
        self.goto(self.xcor(), new_ypos)

    def move_down(self):
        new_ypos = self.ycor() - 20
        self.goto(self.xcor(), new_ypos)
