# -------------------- Black Jack --------------------
import os
import random

clear = lambda:os.system('cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_game = True
while play_game:
    play_game = input("Want to play BlackJack? Type 'y', type 'n' to exit: ")
    clear()
    if play_game == 'y':
        # Your two card
        your_card_value = []
        for i in range(2):
            your_card = random.choice(cards)
            your_card_value.append(your_card)
        print(f"Your cards: {your_card_value}")
        # Computer's first card
        computer_card_value = []
        for j in range(2):
            computer_card = random.choice(cards)
            computer_card_value.append(computer_card)
        print(f"Computer's first card: {computer_card_value[0]}")
        # if computer total to not more than 17
        while sum(computer_card_value) < 17:
            computer_card_value.append(random.choice(cards))
        # You want more card or not
        game_on = True
        while game_on:
            want_more = input("Type 'y' to get another card, type 'n' to pass: ")
            if want_more == 'y':
                your_card_value.append(random.choice(cards))
                # if your sum is more than 21
                if sum(your_card_value) > 21 and your_card_value[-1] == 11:
                    your_card_value[-1] = 1
                    print(f"Your card: {your_card_value}")
                else:
                    print(f"Your card: {your_card_value}")
                if sum(your_card_value) >= 22:
                    print(f"\n\tYour final hand: {your_card_value}")
                    print(f"\tComputer final hand: {computer_card_value}")
                    game_on = False
            elif want_more == 'n':
                print(f"\n\tYour final hand: {your_card_value}")
                print(f"\tComputer final hand: {computer_card_value}")
                game_on = False
        # win loose conditions
        if sum(your_card_value) >= 22:
            print("\n\t---------- You loose, you are up to 21 ----------\n\n")
        elif sum(your_card_value) <= 22 and sum(computer_card_value) >= 22:
            print("\n\t---------- You won ----------\n\n")
        elif sum(your_card_value) > sum(computer_card_value) and sum(computer_card_value) <= 21:
            print("\n\t---------- You Won ----------\n\n")
        elif sum(your_card_value) == sum(computer_card_value):
            print("\n\t---------- Drawww ----------\n\n")
        else:
            print("\n\t---------- Computer won ----------\n\n")
    else:
        print("Exit Successfully!")
        play_game = False
