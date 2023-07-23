from tkinter import *
import math

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


# TODO 4: Generate Timer Reset Function
def reset_timer():
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    canvasT.itemconfig(condition_text, text="TIMER", fill=DARK_GREEN)

    global reps
    reps = 0


# TODO 2: Generate Timer Mechanism
def start_timer():
    global reps
    reps += 1
    work_count = WORK_MIN * 6
    short_count = SHORT_BREAK_MIN * 6
    long_count = LONG_BREAK_MIN * 6

    if reps % 8 == 0:
        count_down(long_count)
        canvasT.itemconfig(condition_text, text="LONG BREAK", fill=LB_COLOR)
    elif reps % 2 == 0:
        count_down(short_count)
        canvasT.itemconfig(condition_text, text="SHORT BREAK", fill=SB_COLOR)
    else:
        count_down(work_count)
        canvasT.itemconfig(condition_text, text="WORK", fill=RED)


# TODO 3: Generate Countdown Function
def count_down(count):
    minute = math.floor(count / 60)
    second = count % 60

    if int(minute) == 0:
        minute = "00"

    if int(second) == 0:
        second = "00"

    if 10 > int(minute) > 0:
        minute = f"0{minute}"

    if 0 < int(second) < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = screen.after(1000, count_down, count - 1)

    else:
        start_timer()


# TODO 1: Create Window and Configurate GUI

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

btn_start = Button(text="Start", command=start_timer, fg="black", bg=YELLOW, font=(FONT_NAME, 16, "bold"),
                   highlightthickness=0)
btn_start.grid(row=3, column=0)

btn_reset = Button(text="Reset", fg="black", command=reset_timer, bg=YELLOW, font=(FONT_NAME, 16, "bold"),
                   highlightthickness=0)
btn_reset.grid(row=3, column=3)

screen.mainloop()