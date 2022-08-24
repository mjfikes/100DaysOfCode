from tkinter import *
from tkinter import messagebox
import pyperclip
import json

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
    new_data = {site:{
            'email':user,
            'password':pw,
        }
    }
    is_ok = messagebox.askyesno(title=site,message=f'These are the details entered: \nEmail: {user}\nPassword:'
                                                f'{pw}\nIs the above information correct?')
    if is_ok:
        try:
            with open('passwords.json','r') as j:
                data = json.load(j)
                data.update(new_data)
            with open('passwords.json','w') as j:
                json.dump(data,j,indent=4)
        except FileNotFoundError:
            with open('passwords.json', 'w') as j:
                json.dump(new_data,j,indent=4)


        finally:

            entry_site.delete(0,END)
            entry_pass.delete(0,END)
    else: return
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_site():
    site = entry_site.get()
    user = entry_email.get()
    pw = entry_pass.get()

    try:
        with open('passwords.json','r') as j:
            data = json.load(j)

            if data.get(site) == None:
                messagebox.showwarning(title='Search Results',message='No results found')
            else:
                messagebox.showinfo(title='Search Results',message=f'{data.get(site)}')

    except FileNotFoundError:
        messagebox.showwarning(title='Search Results',message='No saved passwords found')

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
search_button = Button(text='Search', command=search_site,width=16)
generate_button = Button(text='Generate Password', command=generate_pass,width=16)
add_button = Button(text='Add', command=add_pass,width=30)
search_button.grid(column=2,row=1)
generate_button.grid(column=2,row=3,sticky='w')
add_button.grid(column=1,row=5,columnspan=2,pady=10)
window.mainloop()