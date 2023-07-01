import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creating Game Screen
screen = Screen()
screen.title("Crossy Road Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating player Object from Player Class
player = Player()

# Creating scoreboard Object from Scoreboard Class
scoreboard = Scoreboard()

# Detecting User's Keyboard Touch
screen.listen()
screen.onkey(player.walk, "Up")

# Creating cars Object from CarManager Class
cars = CarManager()

game_over = False
while not game_over:
    # Configuring the Speed of Moving Objects
    time.sleep(cars.speed)
    screen.update()

    # Creating randomly cars on the Game Screen
    cars.create_cars()
    cars.move()

    # Is the Game Over?
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_over = True

    # Level is Completed?
    if player.is_finish():
        scoreboard.next_level()
        cars.increase_speed()


screen.exitonclick()