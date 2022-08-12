from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.p1score = 0
        self.p2score = 0

    def draw_court(self):

        self.hideturtle()
        self.speed(0)
        self.pencolor('white')
        self.pu()
        self.setposition(0, -800)
        self.setheading(90)
        self.pd()
        for i in range(1, int(600 / 20) + 1):
            self.fd(20)
            self.pu()
            self.fd(20)
            self.pd()

    def draw_score(self):
        self.setposition(0,200)
        self.clear()

        self.pencolor('white')
        self.write('{0}   {1}'.format(self.p1score,self.p2score),align='center',font=('Courier',30))

