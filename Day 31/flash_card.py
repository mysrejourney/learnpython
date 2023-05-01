""" Import the required module """
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"  # Background color for the window
current_card = {}  # To store the current card in dictionary format - e.g {'French': 'pensais', 'English': 'thought'}

# --------------------- RANDOM WORD GENERATION --------------------#

######## OPTION 1 ###################
# def next_card():
#     data = pandas.read_csv("french_words.csv")
#     # print(data)
#
#     new_dict = {row.French: row.English for (index, row) in data.iterrows()}
#     print(new_dict)
#     column_headers = {title for title in data.columns}
#     new_header_list = list(column_headers)
#     print(new_header_list[0])
#     random_french_word = random.choice(list(new_dict.keys()))
#     print(random_french_word)
#     canvas.itemconfig(word, text=f"{random_french_word}")
#     canvas.itemconfig(title, text=f"{new_header_list[0]}")

############## OPTION 2 #################
""" Read the data from words_to_learn.csv file. If this file doesn't exists, read the data from french_words.csv file """
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    # original_data is a pandas dataframe object
    original_data = pandas.read_csv("french_words.csv")
    # to_learn is a dictionary {'French': {0: 'partie', 1: 'histoire', 2: 'chercher'}, 'English': {0: 'part', 1: 'history', 2: 'search'}}
    # to_learn = original_data.to_dict() # without orient="records"
    # print(to_learn)
    # orient="records" used to convert pandas dataframe to the list of dictionaries e.g [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}]
    to_learn = original_data.to_dict(orient="records") # it is a list contains dictionary
else:
    to_learn = data.to_dict(orient="records") # it is a list contains dictionary
    # print(to_learn)


def next_card():  # function to display the next card
    global current_card  # Holds current card value is dictionary format
    global flip_timer  # To calculate the timer to flip the card
    window.after_cancel(flip_timer)  # You need to set the flip card time to 0 for each card. So each card will display for 3 seconds and then it flips
    current_card = random.choice(to_learn)  # randomly select a card from the list (to_learn)
    # print(current_card)
    random_french_word = current_card["French"]  # Pick only French word from the randomly selected a card
    canvas.itemconfig(image_card, image=front_image)  # set the image for French word
    canvas.itemconfig(word, text=f"{random_french_word}", fill="black")  # Display randomly selected French word
    canvas.itemconfig(title, text=f"French", fill="black")  # Display the title as French in black color text
    flip_timer = window.after(3000, flip_card)  # Flip the card after 3 seconds


def flip_card():  # Function to use to flip the card after 3 seconds
    random_english_word = current_card["English"]  # Pick only English word from the randomly selected a card
    canvas.itemconfig(image_card, image=back_image)  # set the image for English word
    canvas.itemconfig(word, text=f"{random_english_word}", fill="white")  # Display randomly selected English word
    canvas.itemconfig(title, text=f"English", fill="white")  # Display the title as English in white color text


def is_known():  # Function to remove the card from the original data and save the remaining data to words_to_learn.csv file
    to_learn.remove(current_card)
    # print(len(to_learn))
    next_card()
    # After eliminate the known word, remaining words will go and save it in words_to_learn.csv
    pandas.DataFrame(to_learn).to_csv("words_to_learn.csv", index=False)


# --------------------- UI SETUP ----------------------------------#

""" Window configuration setup """
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

""" Canvas configuration setup """
front_image = PhotoImage(file="card_front.png")  # Set an image as background
back_image = PhotoImage(file="card_back.png")
canvas = Canvas(width=800, height=526)
image_card = canvas.create_image(400, 263, image=front_image)  # Set an image as background for this canvas
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))  # set the initial title text
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))  # set the initial word text
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

""" Right Tick mark configuration setup """
right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

""" Wrong mark configuration setup """
wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()  # While launching the window, automatically picks title and word and display them
window.mainloop()
