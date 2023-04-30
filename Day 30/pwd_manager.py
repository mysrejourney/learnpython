""" Import the required modules """
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# Below module is used to copy the text into the clipboard to paste wherever required
import pyperclip
import json

# -------------------- FIND PASSWORD --------------------------#
def find_password():
    # get the website data entered in website textbox
    website = website_textbox.get()
    try:
        """ Open the file and load the data"""
        with open("data.json", "r") as data_file:
            data = json.load(data_file)  # data is a dictionary
    except FileNotFoundError:
        """ If the file is not found, then display the message box saying No data file found"""
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        # print(data)
        # print(website)
        # print(data.items())
        """ If website is not in the dictionary, then display the message box saying No data found"""
        if website not in data:
            messagebox.showinfo(title="Error", message=f"No data found for {website}")
        else:
            """ Get the email and password and display them in the message box"""
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title="Password Information", message=f"Email is {email}\nPassword is {password}")
    finally:
        website_textbox.delete(0, END)  # Delete the entry in website textbox
        website_textbox.focus()  # Focus website textbox

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
    """ Creating new dictionary with entered values """
    new_data = {
        website_textbox.get(): {
        "Email": email_textbox.get(),
        "Password": password_textbox.get()
        }
    }
    print(new_data)
    """ Check if website and password field is empty """
    if len(password_textbox.get()) <= 0 or len(website_textbox.get()) <= 0 or len(email_textbox.get()) <= 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            """ Write the website, email and password into text file """
            with open('data.json', 'r') as data_file:
                """ Reading the json file """
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                """ Writing the dictionary to the json file """
                json.dump(new_data, data_file, indent=4)
        else:
            """ Update the data """
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                """ Writing the dictionary to the json file """
                json.dump(data, data_file, indent=4)
        finally:
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
website_textbox = Entry(width=24)
website_textbox.insert(0, "")
website_textbox.grid(column=1, row=1)
website_textbox.focus()

""" email label configuration """
email_label = Label(text="Email/Username", font=("courier", 16, "normal"))
email_label.grid(column=0, row=2)

""" email textbox configuration """
email_textbox = Entry(width=35)
email_textbox.insert(0, "satheesh@gmail.com")
email_textbox.grid(column=1, row=2, columnspan=2)

""" password label configuration """
password_label = Label(text="Password", font=("courier", 16, "normal"))
password_label.grid(column=0, row=3)

""" password textbox configuration """
password_textbox = Entry(width=24)
password_textbox.insert(0, "")
password_textbox.grid(column=1, row=3)

""" generate button configuration """
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)

""" search button configuration """
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

""" add button configuration """
add_button = Button(text="Add", width=32, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
