# TODO 1: Create Window and Configurate GUI
from tkinter import *

SB_COLOR = "#1B1A54"
RED = "#790000"
LB_COLOR = "#21FF30"
YELLOW = "#F7F5DD"
DARK_GREEN = "#464B1D"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

screen = Tk()
screen.title("TIME MANAGER")
screen.config(padx=100, pady=50, bg=YELLOW)

canvasT = Canvas(width=260, height=40, bg=YELLOW, highlightthickness=0)
condition_text = canvasT.create_text(130, 20, text="TIMER", fill=DARK_GREEN, font=(FONT_NAME, 40, "bold"))
canvasT.grid(row=0, column=1)

canvas = Canvas(width=240, height=240, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="clock.png")
canvas.create_image(120, 120, image=img)
timer_text = canvas.create_text(120, 130, text="00:00", fill=DARK_GREEN, font=(FONT_NAME, 45, "bold"))
canvas.grid(row=2, column=1)

btn_start = Button(text="Start", fg="black", bg=YELLOW, font=(FONT_NAME, 16, "bold"), highlightthickness=0)
btn_start.grid(row=3, column=0)


btn_reset = Button(text="Reset", fg="black", bg=YELLOW, font=(FONT_NAME, 16, "bold"), highlightthickness=0)
btn_reset.grid(row=3, column=3)

screen.mainloop()

# TODO 2: Generate Timer Mechanism


# TODO 3: Generate Countdown Function


# TODO 4: Generate Timer Reset Function