from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.goto(0, 280)
        self.write(f'Score : {self.score} ', align='center', font=('terminal', 12, 'normal'))

    def get_score(self):
        return self.score

    def show_score(self):
        self.clear()
        self.write(f'Score : {self.score} ', align='center', font=('terminal', 12, 'normal'))

    def add_point(self):
        self.score +=1

    def kill_screen(self):
        self.goto(0, 40)
        self.write('THE SNAKE IS DEAD!', align='center', font=('Terminal', 20, 'normal'))
        self.goto(0,-80)
        self.write(f'FINAL SCORE: {self.score}', align='center', font=('Terminal', 18, 'normal'))
