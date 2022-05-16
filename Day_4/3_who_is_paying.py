import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, seperated by a comma.")

names = namesAsCSV.split(",")

index_finder = random.randint(0, len(names)-1)

person_who_pay = names[index_finder]

print(f"The bill will pay {person_who_pay}")
