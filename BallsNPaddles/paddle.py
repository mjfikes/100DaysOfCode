from turtle import Turtle
SPEED = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(5,1)
        self.speed(0)
        self.color('white')

    def up(self):
        if self.distance(self.xcor(), 300) > 25-SPEED:
            self.sety(self.ycor() + SPEED)

    def down(self):
        if self.distance(self.xcor(),-300)> 25+SPEED:
            self.sety(self.ycor() - SPEED)


