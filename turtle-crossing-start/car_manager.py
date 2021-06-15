from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_car = []
        self.move_position = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            turtle = Turtle(shape="square")
            turtle.penup()
            turtle.color(random.choice(COLORS))
            turtle.goto(300, random.randint(-250, 250))
            turtle.shapesize(stretch_wid=1, stretch_len=2)
            turtle.setheading(180)
            self.all_car.append(turtle)

    def move(self):
        for car in self.all_car:
            car.forward(self.move_position)

    def move_incresa(self):
        self.move_position += MOVE_INCREMENT

