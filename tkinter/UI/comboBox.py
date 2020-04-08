from tkinter import *
from tkinter import ttk

root = Tk()

month = StringVar()
comboBox = ttk.Combobox(root, textvariable = month )
comboBox.pack()

comboBox.config(values = ("Jan", "Feb", "Mar","Apr"))

print(month.get())

# Spin box
year = StringVar()
Spinbox(root, from_ = 1990, to = 2030, textvariable = year ).pack()
mainloop()