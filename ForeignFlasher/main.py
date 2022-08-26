import pandas as pd
from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"
CANVAS_HEIGHT = 900
CANVAS_WIDTH = 800
italian_words = './data/Italian.xlsx'
language_data = pd.read_excel(italian_words)
my_word = language_data.sample(1)
def right_word():
    window.after_cancel(timer)
    language_data.drop(index=my_word.index)
    next_card()


def wrong_word():
    window.after_cancel(timer)
    next_card()

# -----Go to next word
def next_card():
    global my_word
    canvas.itemconfig(card, image=card_front)
    current_word = language_data.sample(1)
    canvas.itemconfig(language_label,text=f'{current_word.columns[1]}',fill='black')
    canvas.itemconfig(word_label,text=current_word[current_word.columns[1]].values[0],fill='black')
    #word_label.config(text=current_word[current_word.columns[1]].values[0],fill='black')
    window.after(3000, flip_card, current_word)
    return(current_word)

def flip_card(word):

    canvas.itemconfig(language_label,text=word.columns[0],fill='white')
    canvas.itemconfig(card,image=card_back)
    canvas.itemconfig(word_label,text=word[word.columns[0]].values[0],fill='white')



# -----Create UI--------------
# Create window and canvas
window = Tk()
window.title('Foreign Flasher')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
# Get images
card_back = PhotoImage(file='./images/card_back.png')
card_front = PhotoImage(file='./images/card_front.png')
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')
canvas.grid(row=0,column=0)
card = canvas.create_image(400,375,image=card_front)
# Labels
language_label = canvas.create_text(350,180,text=language_data.columns[1],font=('Arial',40,'italic'))
#(Label(text=language_data.columns[1],font=('Arial',40,'italic'),bg='white')
word_label = canvas.create_text(350,350,text='',font=('Arial',40,'italic'),justify=CENTER)

#language_label.place(x=350,y=180)

timer = window.after(3000,flip_card,my_word)
# Buttons
right_button = Button(image=right_img, command= right_word, width=100,borderwidth=0,highlightthickness=0)
wrong_button = Button(image=wrong_img, command= wrong_word, width=100,borderwidth=0,highlightthickness=0)
right_button.place(x=250,y=700)
wrong_button.place(x=500,y=700)
# -----Function for Right Answer Button to remove learned word

my_word = next_card()


window.mainloop()
language_data.to_csv('Italian study.csv')