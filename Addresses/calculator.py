from tkinter import *
from math import trunc

root = Tk()
root.title('Calculadora')
root.iconbitmap('C:/Users/ti.infra/Desktop/fsociety.ico')

entry_widget = Entry(root, width=35, borderwidth=5)
entry_widget.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = entry_widget.get()
    entry_widget.delete(0, END)
    entry_widget.insert(0, str(current) + str(number))

def button_clear():
    entry_widget.delete(0, END)

def button_add():
    first_num = entry_widget.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    entry_widget.delete(0, END)

def button_equal():
    last_num = entry_widget.get()
    entry_widget.delete(0, END)
    if math == 'addition':
        entry_widget.insert(0, f_num + int(last_num))
    elif math == 'subtract':
        entry_widget.insert(0, f_num - int(last_num))
    elif math == 'multiply':
        entry_widget.insert(0, f_num * int(last_num))
    elif math == 'divide':
        entry_widget.insert(0, f_num / int(last_num))

def button_subtract():
    first_num = entry_widget.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_num)
    entry_widget.delete(0, END)

def button_multiply():
    first_num = entry_widget.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_num)
    entry_widget.delete(0, END)

def button_divide():
    first_num = entry_widget.get()
    global f_num
    global math
    math = "divide"
    try:
        f_num = int(first_num)
    except ValueError:
        f_num = float(first_num)
    entry_widget.delete(0, END)


# Define Buttons
button_0 = Button(root, text=0, padx=40, pady=20, command=lambda: button_click(0))

button_1 = Button(root, text=1, padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text=2, padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text=3, padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text=4, padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text=5, padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text=6, padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text=7, padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text=8, padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text=9, padx=40, pady=20, command=lambda: button_click(9))


button_equal= Button(root, text='=', padx=86, pady=20, command=button_equal)
button_clear= Button(root, text='Clear', padx=77, pady=20, command=button_clear)

button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_subtract = Button(root, text='-', padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text='*', padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text='/', padx=41, pady=20, command=button_divide)

# Put Buttons on the Screen
button_0.grid(row=4, column=0)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()
