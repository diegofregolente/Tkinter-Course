from tkinter import *

root = Tk()


entry_widget = Entry(root, width=50)
entry_widget.pack()
entry_widget.insert(0, 'Enter Your Name: ')

def myClick():
    hello = 'Hello ' + entry_widget.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text='Enter Your Name', command=myClick)
myButton.pack()


root.mainloop()