import tkinter as t

def button_calculate(miles=0):
    miles = float(entry.get())
    km = round((1.609344 * miles),2)
    labelans.config(text=f'{km}')



window = t.Tk()
window.title('Miles to Km Conversion')
window.minsize(width=150,height=50)
window.config(padx=30,pady=30)


entry = t.Entry(width=10)
entry.grid(column=1,row=0)
labeleq = t.Label(text = 'is equal to')
labeleq.grid(column=0,row=1)
labelmi = t.Label(text = 'Miles')
labelmi.grid(column=2,row=0)
labelkm = t.Label(text = 'Km')
labelkm.grid(column=2,row=1)
labelans = t.Label(text = '')
labelans.grid(column=1,row=1)
button = t.Button(text='Calculate',command=button_calculate)
button.grid(column=1,row=2)


window.mainloop()