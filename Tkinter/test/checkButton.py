from tkinter import *
from tkinter import ttk

root = Tk()


# Check box
checkButton = ttk.Checkbutton(root, text = "Spam?")
spam = StringVar()
checkButton.config(variable = spam, onvalue = "SPAM", offvalue = "NO SPAM")
checkButton.pack()

spam.get()

# Radio button
rb = StringVar()
ttk.Radiobutton(root, text = "text1", variable = rb, value = "TEXT1" ).pack()
ttk.Radiobutton(root, text = "text2", variable = rb, value = "TEXT2" ).pack()
rb.get()
mainloop()
