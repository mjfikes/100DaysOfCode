from turtle import Turtle, Screen
import random

turtle_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []
screen = Screen()
screen.setup(width=500, height=400)
x_pos = -220
y_pos = -150



is_race_on = False

for i in turtle_colors:
    t = Turtle()
    t.pu()
    t.shape('turtle')
    t.shapesize(.8,1)
    t.color(i)
    t.goto(x=x_pos,y=y_pos)
    t.write(i, align='center')
    t.goto(x=x_pos, y=y_pos-10)
    y_pos+=60

    turtle_list.append(t)



user_bet = screen.textinput('Make a bet', prompt='Which turtle will win the race? Enter a color: ')

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtle_list:
        if t.xcor() >= 230:
            winner = t.pencolor()
            is_race_on = False


        else: t.fd(random.randint(1,10))
screen.clear()
[x.hideturtle() for x in turtle_list]
helper_t = Turtle()
helper_t.hideturtle()
helper_t.shape('turtle')
helper_t.pu()
helper_t.setpos(x=0,y=-100)
if winner == user_bet.lower():

    helper_t.write(f"Congratulations, {winner} turtle wins!",align='center')
else:
    helper_t.write(f"Sorry, the {winner} turtle was the winner, not the {user_bet.lower()} turtle.", align='center')
helper_t.color(winner)
helper_t.lt(90)
helper_t.shapesize(5,5)
helper_t.setpos(x=0,y=50)
helper_t.showturtle()
screen.exitonclick()