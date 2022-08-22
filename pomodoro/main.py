from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WIDTH = 224
HEIGHT = 224
CHKMARK = '✓'
reps = 0
timer = None
checklist = []
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clicked():
    window.after_cancel(timer)
    global reps
    reps = 0
    global checklist
    checklist = []
    label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text,text='--:--')


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    sb_sec = SHORT_BREAK_MIN*60
    lb_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        tick(lb_sec)
        label.config(text='Break!', fg=RED)

    elif reps % 2 == 0:

        tick(sb_sec)
        label.config(text='Break!', fg=PINK)
    else:

        tick(work_sec)
        label.config(text='Work!', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def tick(count):

    minutes = math.floor(count/60)
    seconds = round(count% 60,0)
    canvas.itemconfig(timer_text, text=f'{minutes:.0f}:{seconds:0>2.0f}')

    if count >0:
        global timer
        timer = window.after(1000,tick,count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            checklist.append(CHKMARK)
            chk_label.config(text=checklist)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)

checkmark = '✓'
canvas = Canvas(width=WIDTH,height=HEIGHT,bg=YELLOW, highlightthickness=0)
background = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=background)
timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
label = Label(text='Timer', bg=YELLOW,fg=GREEN,font=(FONT_NAME, 48, 'bold'))
chk_label = Label(text=checklist, bg=YELLOW,fg=GREEN,font=(FONT_NAME, 18, 'bold'))


start_button = Button(text='Start', command=start_timer)
reset_button = Button(text='Reset', command=reset_clicked)

label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
chk_label.grid(column=1, row=3)
reset_button.grid(column=2, row=2)

window.mainloop()