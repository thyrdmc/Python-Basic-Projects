from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.clear_board()

    def next_level(self):
        self.goto(0,0)
        self.level += 1
        self.clear_board()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color("black")
        self.write(f"Game Over", align="center", font=FONT)

    def clear_board(self):
        self.clear()
        self.goto(-230, 260)
        self.color("black")
        self.write(f"Level {self.level}", align="center", font=FONT)
