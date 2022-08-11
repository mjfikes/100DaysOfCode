from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('alice blue')
        self.goto(0, 0)
        self.momentum = 10
        self.setheading(45)

    def move(self):
        self.forward(self.momentum)

    def bounce(self):
        self.setheading(abs(self.heading()-360))
        self.forward(self.momentum+4)

    def deflect(self):
        deviation = 90-random.randint(1,10)
        self.setheading(abs(self.heading()-deviation))
        self.forward(self.momentum + random.randint(3,10))
