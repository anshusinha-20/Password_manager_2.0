"""imported every class from the tkinter module"""
from tkinter import *

"""constant"""
FONT = ("Courier", 20, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# window

"""created the window object"""
window = Tk()
window.title("Password manager")
window.config(padx=100, pady=100)

# canvas

"""created the canvas object"""
canvas = Canvas(width=200, height=200)
logoImage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImage)
canvas.grid(row=1, column=2)

# label

"""created the labelWebsite object"""
labelWebsite = Label(text="Website:", font=FONT)
labelWebsite.grid(row=2, column=1)

"""created the labelEmailUsername object"""
labelEmailUsername = Label(text="Email/Username:", font=FONT)
labelEmailUsername.grid(row=3, column=1)

"""created the labelPassword object"""
labelPassword = Label(text="Password:", font=FONT)
labelPassword.grid(row=4, column=1)

# entry

"""created the entryWebsite object"""
entryWebsite = Entry(width=35)
entryWebsite.grid(row=2, column=2, columnspan=2)

"""created the entryEmailUsername object"""
entryEmailUsername = Entry(width=35)
entryEmailUsername.grid(row=3, column=2, columnspan=2)

"""created the entryPassword object"""
entryPassword = Entry(width=20)
entryPassword.grid(row=4, column=2)

# button

"""created the buttonPassword object"""
buttonPassword = Button(text="Generate Password", width=11)
buttonPassword.grid(row=4, column=3)

"""created the buttonAdd object"""
buttonAdd = Button(text="Add", width=32)
buttonAdd.grid(row=5, column=2, columnspan=2)


"""loop to keep the window open"""
window.mainloop()
