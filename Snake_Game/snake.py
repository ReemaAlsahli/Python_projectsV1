from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("green")
        tim.shapesize(stretch_wid=0.5, stretch_len=0.5)
        tim.speed("slowest")
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments)-1, 0, -1):
            x_new = self.segments[segment-1].xcor()
            y_new = self.segments[segment-1].ycor()
            self.segments[segment].goto(x_new, y_new)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for seg in self.segments:
             seg.goto(10000,10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]