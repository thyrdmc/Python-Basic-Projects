from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEED = 7


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = 0.1

    def create_cars(self):
        car_number = random.randint(1,6)
        if car_number == 3:
            turtle = Turtle()
            turtle.shape("square")
            turtle.shapesize(1, 2)
            turtle.penup()
            turtle.color(random.choice(COLORS))
            turtle.goto(x=350, y=random.randint(-250, 250))
            self.all_cars.append(turtle)

    def move(self):
        for _ in self.all_cars:
            _.backward(SPEED)

    def increase_speed(self):
        for _ in self.all_cars:
            self.speed *= 0.99
