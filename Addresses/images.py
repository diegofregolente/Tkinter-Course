from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Batman')
root.iconbitmap('C:/Users/ti.infra/Desktop/batman.ico')

batmanImage = ImageTk.PhotoImage(Image.open('c:/users/ti.infra/desktop/batvssuper.jpg'))
mLabel = Label(image=batmanImage)
mLabel.pack()

button_quit = Button(root, text='Sair do Programa', command=root.quit)
button_quit.pack()

root.mainloop()
