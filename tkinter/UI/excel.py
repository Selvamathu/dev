from tkinter import * 
from tkinter import ttk

# It is a windoe
window = Tk()

# Window title
window.title("My First App")

# window size
window.geometry("350x200")

# Add Label
lbl = ttk.Label(window, 
                text = "Hello", 
#                 font = ("Arial Bold",50)
                )
lbl.grid( row = 0, column = 0)
                
# when button is clicked      
def clicked():
    lbl.configure(text = "Button is clicked")   
     
# Add button
ttk.Button(  window,
             text = "Click Me",
             command = clicked
             ).grid( row = 1, column = 0)




window.mainloop()