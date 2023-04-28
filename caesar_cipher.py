from ascii_logos import caesar_cipher_logo

print(caesar_cipher_logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesar_cipher(text, shift, direction):
    new_text = ''
    shift %=26

    if direction == 'decode':
        shift *= -1
    for i in text:

        if i in alphabet:
            x = alphabet.index(i)
            print(f'{i} -- {x}')
            if x+shift > 25:
                new_text += alphabet[x+shift-26]
            elif x+shift < 0:
                new_text += alphabet[x+shift+26]
            else:
                new_text += alphabet[x+shift]
        else:
            new_text += i

    print(f"The {direction}d text is {new_text}")


should_end = False

while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if restart == 'no':
        should_end = True
        print('Good Bye, we look forward to seeing you again.')
    