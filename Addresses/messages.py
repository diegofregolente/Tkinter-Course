from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.title('Batman')
root.iconbitmap('images/batman.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno('This is Popup', 'Hello World') # 1 for Yes 0 for No
    if response == 1:
        Label(root, text='You clicked Yes').pack()
    else:
        Label(root, text='You clicked No').pack()


Button(root, text='Popup', command=popup).pack()

root.mainloop()