def greet(name):
    print(f"Hello {name}!")
    print(f"How are you {name}?")
    print("Let's go to the library!")

greet(name="Angela") # Here name is a parameter and "Angela" is a argument
greet("Jack") # We can also use this

# Multiple parameter-------------------------------------

def greet_with(name, location):
    print(f"Hello there, I am {name}")
    print(f"I am a it guy from {location}")


greet_with("Li Pon", "Bangladesh")
greet_with(name="Seikh", location="Dubai")
