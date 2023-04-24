""" Import the required modules """
from tkinter import *
import math

""" Calculate function to be invoked when calculate button is clicked """


def calculate():
    miles_value = float(
        input_text.get())  # get the value from the textbox and convert it to floating number from string
    km_value = math.ceil(miles_value * 1.60934)  # Multiply with 1.60934 and ceil it to next largest number
    num_label.config(text=km_value)  # Update the kilometer value and display it in GUI


""" Create window object using Tk class """
window = Tk()
window.title("Miles to Km Converter")  # Add the windows title
window.config(width=500, height=300)  # set the window size
window.config(padx=20, pady=20)  # set the window padding

""" Create the input textbox """
input_text = Entry(width=4)
input_text.insert(0, "0")  # set the default value as "0" in the textbox
input_text.grid(column=2, row=1)  # place the widget in the specified location

""" Create the 'miles' label """
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)  # place the widget in the specified location

""" Create the 'is equal to' label """
equal_label = Label(text="is equal to")
equal_label.grid(column=1, row=2)  # place the widget in the specified location

""" Create the 'num label' label """
num_label = Label(text="0")
num_label.grid(column=2, row=2)  # place the widget in the specified location

""" Create the 'km label' label """
km_label = Label(text="Km")
km_label.grid(column=3, row=2)  # place the widget in the specified location

""" Create the calculate button """
button = Button(text="Calculate", command=calculate)  # Call calculate function when this button is clicked
button.grid(column=2, row=3)  # place the widget in the specified location

""" To make sure the window is opened all the time """
window.mainloop()
