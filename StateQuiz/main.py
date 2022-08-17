from turtle import Screen, Turtle
import pandas as pd
import random
import time

BG_PIC = 'blank_states_img.gif'
STATE_CSV = '50_states.csv'

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.goto(0,0)
screen = Screen()
screen.setup(height=491,width=725)
screen.title("US States Guessing Game")
screen.bgpic(BG_PIC)
data = pd.read_csv('50_states.csv')
valid_states = data['state'].to_list()
game_on = True
score = 0

while game_on:
    if score == 50:
        turtle.goto(0,0)
        turtle.write('You win!',font=('Arial',40),align='center')
        game_on = False
        break
    guess = screen.textinput(f'Score: {score}/50', 'Enter Guess (! to give up): ')
    if guess.title() in valid_states:
        row = data[(data['state']== guess.title())]
        xval = int(row['x'])
        yval = int(row['y'])
        turtle.goto(xval,yval)
        turtle.write(*row['state'].values,font=('Arial',6),align='left')
        score += 1

        valid_states.pop(valid_states.index(guess.title()))
    if guess == '!':
        turtle.goto(0, 0)
        turtle.write(f'GAME OVER\nFinal Score:{score}/50',font=('Arial',20),align='center')
        pd.DataFrame(valid_states).to_csv('Missed States.csv',index=None)
        game_on = False

    if guess == '?':
        turtle.goto(0,0)
        turtle.write(f'{random.choice(valid_states)[0]}',font=('Arial',50))
        time.sleep(2)
        turtle.undo()


screen.exitonclick()