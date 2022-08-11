from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

def tick():
    for action in keys_pressed:
        actions[action]()
    if abs(ball.ycor()) < (screen.window_height() // 2)-14:
        ball.move()
    else:
        ball.bounce()

    if abs(ball.xcor()) >350:
        if (ball.distance(p1) < 100 or ball.distance(p2) < 100):
            ball.deflect()

    screen.update()
    screen.ontimer(tick,frame_delay_ms)


frame_delay_ms = 1000 // 30
actions = dict(
    up1=lambda: p1.up(),
    up2=lambda: p2.up(),
    dn1=lambda: p1.down(),
    dn2=lambda: p2.down(),
)

keys_pressed = set()


def player_paddles():

    pad_1 = Paddle()
    pad_1.setx(-360)
    pad_1.sety(0)
    pad_2 = Paddle()
    pad_2.setx(360)
    pad_2.sety(0)
    return pad_1, pad_2


def draw_line():
    disp_t = Turtle()
    disp_t.hideturtle()
    disp_t.speed(0)
    disp_t.pencolor('white')
    disp_t.pu()
    disp_t.setposition(0, -800)
    disp_t.setheading(90)
    disp_t.pd()
    for i in range(1,int(SCREEN_HEIGHT/20)+1):
        disp_t.fd(20)
        disp_t.pu()
        disp_t.fd(20)
        disp_t.pd()



p1,p2 = player_paddles()

screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('P(y)ong')
draw_line()
ball = Ball()
game_on = True



screen.onkeypress(key='w', fun=lambda: keys_pressed.add('up1'))
screen.onkeypress(key='Up', fun=lambda: keys_pressed.add('up2'))
screen.onkeypress(key='s', fun=lambda: keys_pressed.add('dn1'))
screen.onkeypress(key='Down', fun=lambda: keys_pressed.add('dn2'))
screen.onkeyrelease(key='w', fun=lambda: keys_pressed.remove('up1'))
screen.onkeyrelease(key='Up', fun=lambda: keys_pressed.remove('up2'))
screen.onkeyrelease(key='s', fun=lambda: keys_pressed.remove('dn1'))
screen.onkeyrelease(key='Down', fun=lambda: keys_pressed.remove('dn2'))

screen.listen()
tick()

screen.exitonclick()
