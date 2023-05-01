import os
from ascii_logos import auction_logo

print(auction_logo)

def find_highest_bidder(bidding_record):
    max_price = 0
    for bidder in bidding_record:
        if bidding_record[bidder] > max_price:
            max_price = bidding_record[bidder]
            wonner = bidder
    print(f"{wonner.capitalize()} won the auction by paying {max_price} $.")

print('\t\t\t\t Welcome To The Secret Auction Program')

bidders_stop = False
empty_dic = {}
while not bidders_stop:
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $ "))
    bidders = input("""Are there any other bidders? Type 'yes' or 'no'.
""") 
    
    empty_dic[name] = bid 
    find_highest_bidder(empty_dic)

    os.system('clear')

    if bidders == 'no':
        bidders_stop = True
        find_highest_bidder(empty_dic)
        
    