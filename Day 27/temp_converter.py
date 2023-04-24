from tkinter import *

windows = Tk()
windows.title("Temperature Converter")
windows.config(pady=20, padx=20)


def celcius_to_farenheit():
    celcius_value = int(input_textbox.get())
    farenheit_value = round((celcius_value * 9 / 5) + 32)
    temp_f.config(text=f"{farenheit_value}")


enter_input_label = Label(text="Enter your temperature in C")
enter_input_label.grid(column=0, row=0)

input_textbox = Entry(width=4)
input_textbox.insert(0, "0")
input_textbox.grid(column=1, row=0)

output_label = Label(text=f"Your temperature is")
output_label.grid(column=0, row=1)

temp_f = Label(text="0")
temp_f.grid(column=1, row=1)

convert_button = Button(text="Convert", command=celcius_to_farenheit)
convert_button.grid(column=1, row=2)

windows.mainloop()
