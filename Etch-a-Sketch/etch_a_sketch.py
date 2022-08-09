import turtle


def move_forward():
    tim.fd(18)


def move_back():
    tim.bk(18)


def rotate_left():
    tim.lt(18)


def rotate_right():
    tim.rt(18)


def clear_canvas():
    screen.reset()


def hide_turtle():
    if tim.isvisible():
        tim.hideturtle()
    else:
        tim.showturtle()


tim = turtle.Turtle()
tim.shape('triangle')
tim.shapesize(.2,.2)
screen = turtle.Screen()
screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_back)
screen.onkeypress(key='a', fun=rotate_left)
screen.onkeypress(key='d', fun=rotate_right)
screen.onkey(key='c', fun=clear_canvas)
screen.onkey(key='h', fun=hide_turtle)
screen.onkey(key='q', fun=turtle.bye)
screen.exitonclick()