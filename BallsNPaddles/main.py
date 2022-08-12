#  -----------------IMPORTS
from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

#  ------------------VARIABLES
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
GOAL_MARGINS = 30
frame_delay_ms = 1000 // 30
keys_pressed = set()
actions = dict(
    up1=lambda: p1.up(),
    up2=lambda: p2.up(),
    dn1=lambda: p1.down(),
    dn2=lambda: p2.down(),
    rb=lambda: ball.reset(),
)

#  ---------------FUNCTIONS
def tick():
    scoreboard.draw_score()
    for action in keys_pressed:
        actions[action]()
    if abs(ball.ycor()) <= (screen.window_height() // 2)-14:
        ball.move()
    else:
        ball.bounce()

    if ball.xcor() >350:
        if (ball.distance(p2) <= 60):
            ball.deflect()
        else:
            scoreboard.p1score +=1
            ball.reset()

    if ball.xcor() < -350:
        if (ball.distance(p1) <= 60):
            ball.deflect()
        else:
            scoreboard.p2score += 1
            ball.reset()

    screen.update()
    screen.ontimer(tick, frame_delay_ms)


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

# ---OBJECT INITIALIZING
p1, p2 = player_paddles()
scoreboard = Scoreboard()
screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('P(y)ong')
draw_line()
ball = Ball()
game_on = True

# code to handle key input
screen.onkeypress(key='r', fun=lambda: keys_pressed.add('rb'))
screen.onkeypress(key='w', fun=lambda: keys_pressed.add('up1'))
screen.onkeypress(key='Up', fun=lambda: keys_pressed.add('up2'))
screen.onkeypress(key='s', fun=lambda: keys_pressed.add('dn1'))
screen.onkeypress(key='Down', fun=lambda: keys_pressed.add('dn2'))
screen.onkeyrelease(key='w', fun=lambda: keys_pressed.remove('up1'))
screen.onkeyrelease(key='Up', fun=lambda: keys_pressed.remove('up2'))
screen.onkeyrelease(key='s', fun=lambda: keys_pressed.remove('dn1'))
screen.onkeyrelease(key='Down', fun=lambda: keys_pressed.remove('dn2'))
screen.onkeyrelease(key='r', fun=lambda: keys_pressed.remove('rb'))

screen.listen()
tick()

screen.exitonclick()
