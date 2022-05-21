import os
import random

clear = lambda: os.system('cls')

word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)

random_word_dash = []
for letter in random_word:
    random_word_dash.append("_")

total_life = 10

while "_" in random_word_dash:
    user_guess = input("Guess a letter: ")
    clear()
    if user_guess in random_word_dash:
        total_life -= 1
        print(f"You guess the same word. You loose a life. You have {total_life} life remain")
    for i in range(len(random_word)):
        if user_guess == random_word[i]:
            random_word_dash[i] = user_guess
            if "_" not in random_word_dash:
                print("You win")
                break
    print(random_word_dash)
    if user_guess not in random_word:
        total_life -= 1
        print(f"You guess the wrong word. You have {total_life} life remain")
        if total_life == 0:
            print("You loose. You lost your all life.")
