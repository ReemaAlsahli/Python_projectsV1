from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 16, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(arg=f"score: {self.score} high score:{self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
