alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    encoded_text = ""
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
    # and print the encrypted text.
    for char in text:
        char_position = alphabet.index(char)
        new_char_position = char_position + shift
        # print(alphabet[new_char_position])
        encoded_text += alphabet[new_char_position]
    print(f"The encoded text is {encoded_text}")

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text,shift):
    decoded_text = ""
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
    # and print the encrypted text.
    for char in text:
        char_position = alphabet.index(char)
        new_char_position = char_position - shift
        # print(alphabet[new_char_position])
        decoded_text += alphabet[new_char_position]
    print(f"The encoded text is {decoded_text}")

if direction == 'encode':
    encrypt(text,shift)
else:
    decrypt(text, shift)
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.