from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Creepy Python')
game_on = True
snake = Snake()
food = Food()
screen.listen()
screen.onkeypress(key='w', fun=snake.go_up)
screen.onkeypress(key='Up', fun=snake.go_up)

screen.onkeypress(key='s', fun=snake.go_down)
screen.onkeypress(key='Down', fun=snake.go_down)

screen.onkeypress(key='a', fun=snake.go_left)
screen.onkeypress(key='Left', fun=snake.go_left)

screen.onkeypress(key='d', fun=snake.go_right)
screen.onkeypress(key='Right', fun=snake.go_right)

while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    scoreboard.show_score()

    if snake.head.distance(food) < 15:
        snake.add_segment(scoreboard.get_score())

        food.refresh()
        scoreboard.add_point()
    if abs(snake.head.ycor()) > 280 or abs(snake.head.xcor()) > 280:
        snake.is_alive = False

    if snake.is_alive == False:
        game_on = False
        screen.clear()
        screen.bgcolor('red')
        scoreboard.kill_screen()


screen.exitonclick()
