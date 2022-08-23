from tkinter import *
from tkinter import messagebox
import pyperclip
EMAIL = 'mj.fikes@gmail.com'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)



    print(f"Your password is: {password}")
    entry_pass.insert(END,password)
    pyperclip.copy(password)
    return(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    site = entry_site.get()
    user = entry_email.get()
    pw = entry_pass.get()
    is_ok = messagebox.askyesno(title=site,message=f'These are the details entered: \nEmail: {user}\nPassword:'
                                                f'{pw}\nIs the above information correct?')
    if is_ok:
        with open('passwords.txt','a') as f:
            f.write(f'{site} | {user} | {pw}\n')
        entry_site.delete(0,END)
        entry_email.delete(0,END)
        entry_pass.delete(0,END)
    else: return
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('PassManager')
window.config(padx=50,pady=50,bg='white')
canvas = Canvas(width=200,height=200,bg='white',highlightthickness=0)
# logo
bg_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=bg_img)
canvas.grid(row=0, column=1)

#labels
label_site = Label(text='Website:', bg='white')
label_email = Label(text='Email/Username:', bg='white')
label_pass = Label(text='Password:', bg='white')
label_site.grid(column=0, row=1,sticky='e')
label_site.focus()
label_email.grid(column=0, row=2,sticky='e')
label_pass.grid(column=0, row=3, sticky='e')
#inputs
entry_site = Entry(width=45)
entry_email = Entry(width=45)
entry_pass = Entry(width=25)
entry_site.grid(column=1,row=1,columnspan=2)
entry_email.grid(column=1,row=2,columnspan=2)
entry_email.insert(END,EMAIL)
entry_pass.grid(column=1,row=3,sticky='e')
#buttons
generate_button = Button(text='Generate Password', command=generate_pass)
add_button = Button(text='Add', command=add_pass,width=30)
generate_button.grid(column=2,row=3,sticky='w')
add_button.grid(column=1,row=5,columnspan=2,pady=10)
window.mainloop()