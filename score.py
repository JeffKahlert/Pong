from turtle import Turtle

FONT = ("Calibre", 24, "normal")
ALIGN = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 210)
        self.write(f"{self.l_score}  :  {self.r_score}", font=FONT, align=ALIGN)

    def increase_score(self, side):
        self.clear()
        if side == 'left':
            self.l_score += 1
        if side == 'right':
            self.r_score += 1
        self.goto(0, 210)
        self.write(f"{self.l_score}  :   {self.r_score}", font=FONT, align=ALIGN)