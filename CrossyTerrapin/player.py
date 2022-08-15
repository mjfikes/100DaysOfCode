from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.goto(0,-300)
        self.setheading(90)
        self.movespeed = 20

    def move(self):
        self.forward(self.movespeed)