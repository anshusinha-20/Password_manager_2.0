"""imported every class from the tkinter module"""
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
"""created the window object"""
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

"""created the canvas object"""
canvas = Canvas(width=200, height=200)
logoImage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImage)
canvas.pack()


"""loop to keep the window open"""
window.mainloop()
