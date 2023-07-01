from turtle import Turtle

# Creating Constants
STARTING_POSITION = (0, -280)
STEP = 10
FINISH_LINE_YCOR = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color('green')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def walk(self):
        self.forward(STEP)

    def is_finish(self):
        if self.ycor() == FINISH_LINE_YCOR:
            self.goto(STARTING_POSITION)
            return True



