from turtle import Turtle
import random

class food(Turtle):
    def __init__(self):
        super().__init__()
        self.snake("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("faster")
        self.refresh()
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)