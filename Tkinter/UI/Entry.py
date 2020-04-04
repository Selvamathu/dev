from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text = "Name").pack()
entry = ttk.Entry(root, width = 30)
entry.pack()


button = ttk.Button(root, text = "Enter")
button.pack()


def saveEntry( ):
   text = entry.get() 
   print( text )
    
button.config(command = saveEntry )

mainloop()
