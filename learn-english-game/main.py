import random
from tkinter import *
from tkinter import messagebox

import pandas
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"


screen = Tk()
screen.title("FlashCard")

screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# timer = screen.after(5000, func=flip_language)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="ui-requirements/card_front.png")
back_img = PhotoImage(file="ui-requirements/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="ui-requirements/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="ui-requirements/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

# random_data()

screen.mainloop()