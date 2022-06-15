import os
import random
from art import logo, vs
from game_data import data
clear = lambda: os.system('cls')
point = 0
a = random.choice(data)
print(logo)
play_game = True
while play_game:
    b = random.choice(data)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    a_follower = a['follower_count']
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    b_follower = b['follower_count']
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    clear()
    if guess == 'a' and a_follower > b_follower:
        point += 1
        print(f"You're right! Current score: {point}")
        a = b
        b = random.choice(data)
    elif guess == 'b' and b_follower > a_follower:
        point += 1
        print(f"You're right! Current score: {point}")
        a = b
        b = random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {point}")
        play_game = False
