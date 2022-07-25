from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.refresh()

    def refresh(self):
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        x = random.randint(-280, 280)
        y = random.randint(-280, 270)
        self.goto(x, y)
