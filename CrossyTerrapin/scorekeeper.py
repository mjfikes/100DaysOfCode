from turtle import Turtle

class Scorekeeper(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()


    def draw_score(self):
        self.goto(-280,-280)
        self.color('white')
        self.clear()
        self.write(f'Score: {self.score}',font=('Arial',16))