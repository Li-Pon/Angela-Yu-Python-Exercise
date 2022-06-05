import os

clear = lambda:os.system('cls')

game_store = {}
game_on = True
while game_on:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    game_store[name] = bid
    more_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
    if more_bidder == "yes":
        clear()
    elif more_bidder == "no":
        higest_bid = 0
        for key in game_store:
            if game_store[key] > higest_bid:
                higest_bid = game_store[key]
                name = key
        print(f"The winner is {name} with a bid of {higest_bid}")
        game_on = False
