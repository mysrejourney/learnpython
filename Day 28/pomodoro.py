""" Import the required module """
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK_MARK = "✔"
reps = 0  # Calculate session counting
timer = None  # Update the session cancelled


# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1  # Increase the repetition
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    """ Sessions are calculated like 
        work + short break + work + short break + work + short break + work + long break
        and number of sessions is 8 = 4 work, 3 short break, 1 long break
    """
    # Every 8th session, long break started
    if reps % 8 == 0:
        timer_label.config(text=f"LONG BREAK", fg=RED)  # set the text color as red
        count_down(long_break_sec)
    elif reps % 2 == 0:  # Every alternate session, short break started
        timer_label.config(text=f"SHORT BREAK", fg=PINK)  # set the text color as pink
        count_down(short_break_sec)
    else:  # Every add session, work is started
        timer_label.config(text=f"WORK", fg=GREEN)  # set the text color as green
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)  # Convert the given seconds to min
    count_sec = count % 60  # Convert the given seconds to seconds after min has been excluded

    # If second is less than 10, then it needs to be displayed 09, 08 etc., NOT 9, 8,7
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # To display the canvas text as MIN:SEC
    """ To reduce the count down until it reaches 0 """
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # This method used to delay execution of the function
    else:
        start_timer()  # Start the timer again after each cycle has been done
        marks = ""  # Variable to store the tick mark
        work_session = math.floor(reps / 2)  # Every 2 sessions (Work + Break), the tick mark needs to be added
        for _ in range(work_session):
            marks += "✔"
        tick_label.config(text=f"{marks}")


# ---------------------------- UI SETUP ------------------------------- #

""" Configure the window """
window = Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)

""" Set the background image """
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_img)
""" Create the starting text in the image """
timer_text = canvas.create_text(100, 100, text="00:00", fill="white", font=("Courier", 24, "bold"))  # To display the canvas text, we need to use create_text method
canvas.grid(column=1, row=1)

""" Create Timer label """
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

""" Create start button """
start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, command=start_timer)  #highlightthickness is used to eliminate the shadow of the button
start_button.grid(column=0, row=2)

""" Create reset button """
reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset_time)
reset_button.grid(column=3, row=2)

""" Create tick mark label """
tick_label = Label(highlightthickness=0, fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

window.mainloop()
