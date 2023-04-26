import random

stages = ['''
                                +---+
                                |   |
                                O   |
                               /|\  |
                               / \  |
                                    |
                            =========
''', '''
                                +---+
                                |   |
                                O   |
                               /|\  |
                               /    |
                                    |
                            =========
''', '''
                                +---+
                                |   |
                                O   |
                               /|\  |
                                    |
                                    |
                            =========
''', '''
                                +---+
                                |   |
                                O   |
                               /|   |
                                    |
                                    |
                            =========
''', '''
                                +---+
                                |   |
                                O   |
                                |   |
                                    |
                                    |
                            =========
''', '''
                                +---+
                                |   |
                                O   |
                                    |
                                    |
                                    |
                            =========
''', '''
                                +---+
                                |   |
                                    |
                                    |
                                    |
                                    |
                            =========
''']

word_list = ['pencil', 'computer', 'macbook', 'python', 'engineer']

random_word = random.choice(word_list)
empty_list = []

for rand in random_word:
    empty_list += '-'

print(' --- WELCOME TO HANGMAN GAME. GOOD LUCK :) --- \n')
print(f'Hint: The word you are trying to find consist of {len(random_word)} letters. \n')

game_over = False 
counter = 6

while not game_over:

    guess = input('Guess a letter: ').lower() 

    for i in range(len(random_word)):
        letter = random_word[i]

        if letter == guess:
            empty_list[i] = letter

    print(empty_list)

    # print(stages[counter])

    if guess not in random_word:
        counter -= 1 
        if counter == 0:
            game_over = True
            print('You Lose.')

    print(stages[counter])

    if '-' not in empty_list:
        game_over = True
        print('You win.') 

    
    
