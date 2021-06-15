from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(-200, 250)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def level_incrase(self):
        self.clear()
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)
