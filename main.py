"""imported every class from the tkinter module"""
from tkinter import *

"""imported messagebox class from the tkinter module"""
from tkinter import messagebox

"""constant"""
FONT = ("Courier", 20, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
"""function to store the data in a file"""
def addData():
    website = entryWebsite.get()
    emailUsername = entryEmailUsername.get()
    password = entryPassword.get()

    if len(website) == 0 or len(emailUsername) == 0 or len(password) == 0:
        messagebox.showwarning(message="Please don't leave any fields empty!")
    else:
        isOk = messagebox.askokcancel(message=f"Entered details:\nWebsite: {website}\nEmail/Username: {emailUsername}\nPassword: {password}\nDo you want to save?")

        if isOk:
            with open("data.txt", mode="a") as file:
                file.write(f"{entryWebsite.get()} | {entryEmailUsername.get()} | {entryPassword.get()}\n")
                entryWebsite.delete(0, END)
                entryPassword.delete(0, END)


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
entryWebsite.focus()
entryWebsite.grid(row=2, column=2, columnspan=2)

"""created the entryEmailUsername object"""
entryEmailUsername = Entry(width=35)
entryEmailUsername.insert(0, "anshujuly2@gmail.com")
entryEmailUsername.grid(row=3, column=2, columnspan=2)

"""created the entryPassword object"""
entryPassword = Entry(width=20)
entryPassword.grid(row=4, column=2)

# button

"""created the buttonPassword object"""
buttonPassword = Button(text="Generate Password", width=11)
buttonPassword.grid(row=4, column=3)

"""created the buttonAdd object"""
buttonAdd = Button(text="Add", width=32, command=addData)
buttonAdd.grid(row=5, column=2, columnspan=2)


"""loop to keep the window open"""
window.mainloop()
