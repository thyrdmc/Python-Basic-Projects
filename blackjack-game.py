from ascii_logos import blackjack_logo
import random
import os

def deal_card():
    """ Return random card from the cards """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
    card = random.choice(cards)
    
    return card

def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the cards """
    if  sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw ;("
    elif computer_score == 0:
        return "Lose, opponent has BlackJack."
    elif user_score == 0:
        return "Win with a BlackJack."
    elif user_score > 21:
        return "You went over. You lose." 
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    print(blackjack_logo)
    your_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        your_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(your_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\t Your cards: {your_cards}, current score: {user_score}")
        print(f"\t Computer's first card: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if get_another_card == 'y':
                your_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0  and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\t Your final hands: {your_cards}, final score: {user_score}")

    print(f"\t Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you wanna play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    
    os.system('cls||clear')
    play_game()
