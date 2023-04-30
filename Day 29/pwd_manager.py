""" Import the required modules """
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# Below module is used to copy the text into the clipboard to paste wherever required
import pyperclip


# ------------------------ PASSWORD GENERATOR -----------------#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    """ Randomly pick 8 - 10 letters from the letters list """
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    """ Randomly pick 2 - 4 numbers from the numbers list """
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    """ Randomly pick 2 - 4 symbols from the symbols list """
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    """ Add all the above lists and store it in a new list"""
    new_password_list = password_list + number_list + symbol_list
    # shuffle the newly created list. This should have the list which contains all random letters, numbers, symbols mixed up
    shuffle(new_password_list)

    password = "".join(new_password_list) # Join all random letters, numbers, symbols from list to string
    # print(password)
    """ Delete the password string from the textbox """
    password_textbox.delete(0, END)
    """ Insert the generated password into password textbox """
    password_textbox.insert(0, password)
    """ Copy the password into clipboard, which can be pasted wherever needed """
    pyperclip.copy(password)


# --------------------- SAVE THE DATA -------------------------#
def add_data():
    """ Check if website and password field is empty """
    if len(password_textbox.get()) <= 0 or len(website_textbox.get()) <= 0 or len(email_textbox.get()) <= 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        """ Ask the user confirmation if it can for saving the data """
        msg_box = messagebox.askokcancel(title="Confirmation",
                                         message=f"These are the detailes entered: \nEmail: {email_textbox.get()} \nPassword: {password_textbox.get()} \nAre you sure you want to save the information?")
        # msg_box = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to save the information?', icon='warning')
        if msg_box:  # msg_box is a boolean
            """ Write the website, email and password into text file """
            with open('readme.txt', 'a') as f:
                f.write(f"{website_textbox.get()} | {email_textbox.get()} |  {password_textbox.get()} \n")
                website_textbox.delete(0, END)  # Delete the string from website textbox
                password_textbox.delete(0, END)  # Delete the string from password textbox


# ----------------- UI SET UP ---------------------------------#
""" Window setup """
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

""" Image background setup """
logo_img = PhotoImage(file="logo.png")

""" Canvas creation for image background """
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

""" website label configuration """
website_label = Label(text="Website", font=("courier", 16, "normal"))
website_label.grid(column=0, row=1)

""" website textbox configuration """
website_textbox = Entry(width=35)
website_textbox.insert(0, "Enter the website name to generate password for")
website_textbox.grid(column=1, row=1, columnspan=2)  # columnspan will go for across column (merges the columns)
website_textbox.focus()

""" email label configuration """
email_label = Label(text="Email/Username", font=("courier", 16, "normal"))
email_label.grid(column=0, row=2)

""" email textbox configuration """
email_textbox = Entry(width=35)
email_textbox.insert(0, "Enter your email id")
email_textbox.grid(column=1, row=2, columnspan=2)

""" password label configuration """
password_label = Label(text="Password", font=("courier", 16, "normal"))
password_label.grid(column=0, row=3)

""" password textbox configuration """
password_textbox = Entry(width=24)
password_textbox.insert(0, "Enter your password")
password_textbox.grid(column=1, row=3)

""" generate button configuration """
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)

""" add button configuration """
add_button = Button(text="Add", width=32, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
