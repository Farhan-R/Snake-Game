from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("pink")
        self.head.shape("arrow")

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.speed(7)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def add_tail(self):
        pos = self.segments[-1].position()
        self.add_segment(pos)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            next_pos = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(next_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
