from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Creepy Python')
game_on = True
snake = Snake()
screen.listen()

while game_on:

    screen.onkeypress(key='w', fun=snake.go_up)
    screen.onkeypress(key='Up', fun=snake.go_up)

    screen.onkeypress(key='s', fun=snake.go_down)
    screen.onkeypress(key='Down', fun=snake.go_down)

    screen.onkeypress(key='a', fun=snake.go_left)
    screen.onkeypress(key='Left', fun=snake.go_left)

    screen.onkeypress(key='d', fun=snake.go_right)
    screen.onkeypress(key='Right', fun=snake.go_right)
    screen.exitonclick()
