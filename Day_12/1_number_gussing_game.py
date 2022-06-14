import random

computer_guess = random.randint(1,100)

print("Welcome to the Number Gussing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
elif difficulty == 'hard':
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")


while attempts != 0:
    guess = int(input("Make a guess: "))
    if guess > computer_guess:
        attempts -= 1
        print("Too high.")
        if attempts == 0:
            print("You've run out of guesses, you lose")
        else:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
    if guess < computer_guess:
        attempts -= 1
        print("Too low.")
        if attempts == 0:
            print("You've run out of guesses, you lose")
        else:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
    if guess == computer_guess:
        print(f"\n\n\tYou got it! The answer was {guess}.\n\n")
