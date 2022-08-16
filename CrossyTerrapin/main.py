from turtle import Screen, Turtle
from vehicle import Vehicle
from player import Player
from scorekeeper import Scorekeeper
import time

cars_spawned = []
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('snow4')
screen.tracer(0)
screen.title('Crossy Terrapin')
spawn_rate = 6
frame = 0
game_on = True
player = Player()
painter = Turtle()
scorekeeper = Scorekeeper()

def screenrect(height):
    painter.setheading(90)
    painter.begin_fill()
    painter.forward(height)
    painter.rt(90)
    painter.forward(600)
    painter.rt(90)
    painter.forward(height)
    painter.rt(90)
    painter.forward(650)
    painter.end_fill()

def draw_level():
    painter.penup()
    painter.goto(-300, -300)
    painter.color('green')
    painter.fillcolor('green')
    screenrect(60)

    painter.goto(-300, 260)
    screenrect(40)




def spawn_car():
    car = Vehicle()
    for cars in cars_spawned:
        if cars.ycor() == car.ycor():

            car.setx(car.xcor()+50)
    cars_spawned.append(car)


screen.onkeypress(key='w', fun=player.move)
screen.onkeyrelease(key='w', fun=player.stop)

screen.listen()
draw_level()
while game_on:
    screen.update()
    scorekeeper.draw_score()
    if player.ycor()>270:
        scorekeeper.score +=1
        spawn_rate += 1
        player.goto(0, -280)

    for cars in cars_spawned:
        cars.move()
        if cars.distance(player) <30:
            print("SMASH!")
            exit()
    time.sleep(0.05)
    frame += 1
    if frame >= spawn_rate:
        spawn_car()
        frame = 0


screen.exitonclick()

