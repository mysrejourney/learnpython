""" Import the required modules """
from tkinter import *
import requests


def get_quote():  # To get the quote using API
    response = requests.get(url="https://api.kanye.rest/")  # Get the response of this api
    response.raise_for_status()  # Raise any issues based on status code
    result = response.json()  # convert the response to JSON format (Basically a dictionary)
    quote = result["quote"]  # Get the value of quote key
    bg_canvas.itemconfig(quote_text, text=f"{quote}")  # Update the canvas with new quote

""" Window UI set up """
window = Tk()
window.title("Kanye says")
window.config(padx=50, pady=50)

""" Canvas set up """
bg_canvas = Canvas(width=300, height=414)
bg_image = PhotoImage(file="background.png")
bg_canvas.create_image(150, 207, image=bg_image)
quote_text = bg_canvas.create_text(150, 207, text="My QUOTE", fill="white", font=("Arial", 30, "bold"), width=250)  # width is mentioned to wrap the text.
bg_canvas.grid(row=0, column=0)

""" Button set up """
kanye_image = PhotoImage(file="kanye.png")
button = Button(image=kanye_image, highlightthickness=0, command=get_quote)
button.grid(row=1, column=0)

window.mainloop()