from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='Olhe, Eu cliquei no botão!')
    myLabel.pack()

myButton = Button(root, text='Clique aqui', command=myClick, fg="red")
myButton.pack()

root.mainloop()
