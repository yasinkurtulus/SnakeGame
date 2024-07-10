import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x=random.randint(-250,250)
        random_y=random.randint(-250,250)
        self.goto(random_x,random_y)