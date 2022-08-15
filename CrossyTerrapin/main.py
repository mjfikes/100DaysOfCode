from turtle import Screen, Turtle
from vehicle import Vehicle
from player import Player

import time

cars_spawned = []
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('white')
screen.tracer(0)
screen.title('Crossy Terrapin')
frame_delay_ms = 30
SPAWN_RATE = 8
frame = 0
game_on = True
player = Player()

def spawn_car():
    car = Vehicle()
    for cars in cars_spawned:
        if cars.ycor()==car.ycor():

            car.setx(car.xcor()+50)
    cars_spawned.append(car)



screen.onkeypress(key='Up', fun=player.move())
screen.listen()
while game_on:

    for cars in cars_spawned:
        cars.move()
    time.sleep(0.05)
    frame+=1
    if frame >=SPAWN_RATE:
        spawn_car()
        frame = 0

    screen.update()


screen.exitonclick()

