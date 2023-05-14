from ascii_logos import guess_number
import random

def loooper(level):
    """For detect number of attempts"""
    if level == 'easy':
        return 10
    else:
        return 5

def controller(user_number, random_number):
    """Checks the match between two numbers"""
    if user_number == random_number:
        return 0
    elif user_number > random_number:
        return 'To High'
    else:
        return 'To Low'
    
# print(guess_number)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(0,100)

print(number)

choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

lp = loooper(choose_level)

print(f"You have {lp} attempts remanining to guess the number.")

game_over = False
while(lp>0 and not game_over):
    
    user_number = int(input('Make a guess: '))
    if controller(user_number, number) == 0:
        print(f"Congrats, You got it! The answer was {number}")
        game_over = True
    else:
        print(controller(user_number, number))
        print("Guess again.")
    
    lp -= 1
    if lp == 0:
        print("You've run out of guesses, you lose.")
        game_over = True