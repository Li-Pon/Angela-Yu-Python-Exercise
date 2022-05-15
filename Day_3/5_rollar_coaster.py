print("Welcome to the Rollar Coaster.")

height = int(input("Enter your height in cm: "))

if height < 120:
    print("You can not ride.")
    quit()

age = int(input("Enter your age: "))
photo = input("Want photo? Y or N? ").lower()

bill = 0

if age < 12:
    bill += 5
elif age <= 18:
    bill += 7
elif age > 45 and age < 55:
    bill += 0
else:
    bill += 12

if photo == "y":
    bill += 3

print(f"Your total bill is {bill}")
