print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
percentage = int(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
person = int(input("How many people to split the bill? "))

total_bill = round((bill+((bill*percentage)/100))/person, 2)

print(f"Each person should pay: ${total_bill}")
