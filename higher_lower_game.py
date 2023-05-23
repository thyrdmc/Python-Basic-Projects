from ascii_logos import higher_lower_logo, vs
from higher_lover_game_dataset import data

import random
import os

def mixer(random_index_a,random_index_b):
    os.system('clear')
    print(higher_lower_logo)
    print(f"You're right! Current score: {score}")
    print(f"Compare A: {data[random_index_a]['name']}, a {data[random_index_a]['description']}, from {data[random_index_a]['country']} ")
    print(vs)
    print(f"Against B: {data[random_index_b]['name']}, a {data[random_index_b]['description']}, from {data[random_index_b]['country']} ")

    print('\n')

# Print Game Logo
print(higher_lower_logo)

score = 0 
random_index_a = random.randrange(len(data)-1)

# Compare A informations
print(f"Compare A: {data[random_index_a]['name']}, a {data[random_index_a]['description']}, from {data[random_index_a]['country']} ")

# vs logo
print(vs)

random_index_b = random.randrange(len(data)-1)

# Against B informations
print(f"Against B: {data[random_index_b]['name']}, a {data[random_index_b]['description']}, from {data[random_index_b]['country']} ")

game_over = False

while not game_over:
    # selection: Who has more followers? Type 'A' or 'B':
    selection = input("Who has more followers? Type 'A' or 'B': ").upper()

    if selection == 'A' and data[random_index_a]['follower_count'] > data[random_index_b]['follower_count']:
        score += 1 
        
        random_index_a = random_index_b
        random_index_b = random.randrange(len(data)-1)

        mixer(random_index_a, random_index_b)
        

    elif selection == 'B' and data[random_index_b]['follower_count'] > data[random_index_a]['follower_count']:
        score += 1 

        random_index_b = random.randrange(len(data)-1)

        mixer(random_index_a, random_index_b)

    else:
        print(f"Sorry, that's wrong. Final score {score}.")
        game_over = True
    
# if selection is true print You're right! Current score: 2.
# Not selected goes Compare A