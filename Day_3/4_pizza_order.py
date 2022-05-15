print("Welcome to Python Piza Deliveries!")

size = input("What size pizza do you want? S, M or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    elif size == "m" or size == "l":
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your pizza bill is ${bill}")
