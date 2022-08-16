from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.shapesize(.9,.9)
        self.color('lawn green')
        self.goto(0,-280)
        self.setheading(90)
        self.move_speed = 10

    def move(self):

        self.forward(self.move_speed)

    def stop(self):

        self.forward(0)
