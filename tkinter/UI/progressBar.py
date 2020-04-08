from tkinter import *
from tkinter import ttk

root = Tk()
progressBar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200 )
progressBar.pack()

# when we don't know no of steps
# progressBar.config(mode = "indeterminate")
# progressBar.start()
# progressBar.stop()

# When we know the steps
progressBar.config(mode = "determinate", maximum = 11, value = 5)

value = DoubleVar()
# Scale
scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_ = 0.0, to = 11.0)
scale.pack()

scale.set(5.6)

mainloop()
