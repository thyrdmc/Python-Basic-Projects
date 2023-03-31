import random
from random import shuffle

#Dataset 
 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Interact with the User 

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pw_list = [] 

for i in range(nr_letters):
    random_number = random.randint(0, len(letters)-1)
    pw_list.append(letters[random_number])

for i in range(nr_symbols):
    random_number = random.randint(0, len(symbols)-1)
    pw_list.append(symbols[random_number])

for i in range(nr_numbers):
    random_number = random.randint(0, len(numbers)-1)
    pw_list.append(numbers[random_number])

# Shuffling to List

shuffle(pw_list)

#List to String Conversion

password = ''

for j in pw_list:
    password += j

print(f'Your password is {password}')