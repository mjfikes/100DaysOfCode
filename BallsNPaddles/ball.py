from turtle import Turtle
import random
LAUNCH_DIRS = [45, 135, 225, 315]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('alice blue')
        self.goto(0, 0)
        self.momentum = 10
        self.setheading(225)
        self.lastxpos = self.xcor()
        self.lastypos = self.ycor()

    def move(self):
        self.lastxpos = self.xcor()
        self.lastypos = self.xcor()
        self.forward(self.momentum)

    def bounce(self):
        self.setheading(abs(self.heading()-360))
        self.forward(self.momentum+4)

    def deflect(self):
        print(self.lastxpos,self.lastypos)
        print(self.xcor(), self.ycor())
        if self.lastypos - self.ycor() < 0:
            if self.lastxpos - self.xcor() < 0:
                print('x-y-')
                self.setheading(abs(self.heading()-180)) #works?
            else:
                print('y-x+')

                self.setheading(abs(self.heading() - 90)) #works
        else:
            if self.lastxpos - self.xcor()<0:
                print('y+x-')
                self.setheading(abs(self.heading() - 270))
            else:
                print('y+x+')
                print(self.heading())
                self.setheading(abs(self.heading() - 270))

        self.momentum += 2.5
        self.forward(self.momentum + random.randint(3,10))


    def reset(self):
        self.goto(0, 0)
        self.momentum = 10
        #self.setheading(random.choice(LAUNCH_DIRS))
        self.setheading(225)
