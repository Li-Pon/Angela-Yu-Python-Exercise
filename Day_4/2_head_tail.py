import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

head_or_tail = random.randint(0, 1)

if head_or_tail == 0:
    print("Heads")
elif head_or_tail == 1:
    print("Tails")
