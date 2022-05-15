print("Welcome to the Love Calculator.")

name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

names = name1 + name2

count_t = names.count("t")
count_r = names.count("r")
count_u = names.count("u")
count_e = names.count("e")
count_l = names.count("l")
count_o = names.count("o")
count_v = names.count("v")

love_score = int(str(count_t+count_r+count_u+count_e) +
                 str(count_l+count_o+count_v+count_e))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
