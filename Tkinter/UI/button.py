'''
Created on Apr 4, 2020

@author: admin
'''

from tkinter import *
from tkinter import ttk
root = Tk()
# Label
# label = ttk.Label(root, text = "click me")
# label.pack()
# mainloop()

# button
button = ttk.Button(root, text = "Click Me")
button.pack()
def callback():
    print("Clicked")

# button event
button.config(command = callback)

# Disable button
button.state(["disabled"])

# Enable button
button.state(["!disabled"])

mainloop()

