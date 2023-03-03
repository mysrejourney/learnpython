from art import logo

# print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser_cipher(text, shift):
    encoded_text = ""
    for char in text:
        if char in alphabet:
            char_position = alphabet.index(char)
            if direction == 'encode':
                new_char_position = char_position + shift
            else:
                new_char_position = char_position - shift
            encoded_text += alphabet[new_char_position]
        else:
            encoded_text += char
    print(f"The {direction}d text is {encoded_text}")


is_game_on = True
while is_game_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift %= 26
    print(shift)
    caeser_cipher(text,shift)
    result = input("Type 'yes' if you want to go again, else type 'No' \n").lower()
    if result == 'no':
      is_game_on = False
      print("Good bye")