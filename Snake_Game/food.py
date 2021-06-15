from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.refresh()

    def refresh(self):
        new_x = random.randint(-270, 270)
        new_y = random.randint(-270, 270)
        self.goto(new_x, new_y)
