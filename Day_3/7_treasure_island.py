print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")

road = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
if road == "left":
    lake = input(
        "You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if lake == "wait":
        house = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one one blue. Which colour do you choose? 'red', 'blue' or 'green'? ")
        if house == "green":
            print("Congratulation!! You get the price.")
        elif house == "red":
            print("You enter a room full of Lion. Game Over.")
        elif house == "blue":
            print("You enter a room full of King Cobra.")
        else:
            print("Game Over")
    elif lake == "swim":
        print("The river is full of crocodile. Game Over.")
else:
    print("You choose wrong path. Game Over.")
