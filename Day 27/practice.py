import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Satheesh", font=("Calibre", 24, "normal"))
# my_label.pack()
my_label.grid(column=1, row=1)

# my_label["text"] = "New Text"
#my_label.config(text="Adhira")

def button_clicked():
    # my_label.config(text="Button Clicked")
    my_label.config(text=input.get())
    print("Sats")

button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=2, row=2)

button_1 = tkinter.Button(text="New Button")
button_1.grid(column=3, row=1)
#
input = tkinter.Entry(width= 10)
# input.pack()
input.grid(column=4, row=3)
window.mainloop()

################################

# def my_function(a, b=2, c=3):
#     print(f" a= {a + 1}, b = {b + 1}, c={c + 1}")
#
# my_function(4)

#################################

# def add(*args):
#     # print(args)
#     total = 0
#     for num in args:
#         total += num
#
#     return total
#
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

#################################

# def calculate(**kwargs):
#     # for (key, value) in kwargs.items():
#     #     print(key)
#     #     print(value)
#     print(kwargs["multiply"])
#
#
# calculate(add=5, multiply=10)
