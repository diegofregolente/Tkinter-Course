from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Batman')
root.iconbitmap('images/batman.ico')

MODES = [
    ('Pepperoni', 'Pepperoni'),
    ('Mushroom', 'Mushroom'),
    ('Cheese', 'Cheese'),
    ('Onion', 'Onion')
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def click(value):
    label = Label(root, text=value).pack()


# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda :click(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda :click(r.get())).pack()

#label = Label(root, text=pizza.get()).pack()

button = Button(root, text='Click Me', command=lambda :click(pizza.get())).pack()

root.mainloop()