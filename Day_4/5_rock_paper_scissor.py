import random

option = ["Rock", "Paper", "Scissors"]
user_choice = int(
    input("What do you choose?\nType 0 for Rocks, 1 for Paper or 2 for Scissors."))

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number, you lose!")
    quit()

computer_choice = random.randint(0, 2)
print(
    f"\tUser Choice = {option[user_choice]}\n\tComputer Choice = {option[computer_choice]}")

if user_choice == 0:
    if computer_choice == 0:
        print("Draw")
    elif computer_choice == 1:
        print("Computer win")
    elif computer_choice == 2:
        print("User win")

if user_choice == 1:
    if computer_choice == 0:
        print("User win")
    elif computer_choice == 1:
        print("Draw")
    elif computer_choice == 2:
        print("Computer win")

if user_choice == 2:
    if computer_choice == 0:
        print("Computer win")
    elif computer_choice == 1:
        print("User win")
    elif computer_choice == 2:
        print("Draw")
