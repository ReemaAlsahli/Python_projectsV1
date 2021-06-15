from turtle import Turtle
MOVE = 30

class Paddle(Turtle):

    def __init__(self,x_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_position, 0)

    def up(self):
        x_new = self.xcor()
        y_new = self.ycor() + MOVE
        self.goto(x_new, y_new)

    def down(self):
        x_new = self.xcor()
        y_new = self.ycor() - MOVE
        self.goto(x_new, y_new)
