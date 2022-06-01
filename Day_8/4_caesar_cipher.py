alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c',
'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    mod_text = ""
    for char in text:
        if char in alphabet:
            if direction == 'encode':
                mod_text += alphabet[alphabet.index(char) + shift%25]
            elif direction == 'decode':
                mod_text += alphabet[alphabet.index(char) - shift%25]
        else:
            mod_text += char
    print(f"The {direction}d text is {mod_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text=text, shift=shift, direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if result == 'no':
        should_continue = False
