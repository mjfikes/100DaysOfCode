from turtle import Turtle, register_shape
import random

STARTING_SPEED = 10
car_list = ['blue_car.gif', 'red_car.gif', 'green_car.gif', 'yellow_car.gif']

class Vehicle(Turtle):
    def __init__(self):
        super().__init__()
        self.car_file = random.choice(car_list)
        self.penup()
        self.speed = STARTING_SPEED
        #self.shape('car.gif')
        register_shape(self.car_file)
        self.shape(self.car_file)
        self.setheading(180)
        self.goto(400, random.randrange(-200,250,60))

    def move(self):
        self.forward(self.speed)
