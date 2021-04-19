from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Batman')
root.iconbitmap('images/batman.ico')
root.geometry('400x200')

def graph():
    housePrices = np.random.normal(200000, 25000, 5000)
    plt.pie(housePrices)
    plt.show()


myButton = Button(root, text='Show Graph', command=graph)
myButton.pack()
root.mainloop()