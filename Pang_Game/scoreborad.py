from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(100, 250)
        self.write(f"{self.r_score}", align=ALIGN, font=FONT)

    def increse_l(self):
        self.l_score += 1
        self.update()

    def increse_r(self):
        self.r_score += 1
        self.update()