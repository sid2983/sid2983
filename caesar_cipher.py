from sympy import im
from caesar_art import logo
print(logo+"\n\n")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',' ', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type 'encode' to encrypt or 'decode' to decrypt the message : ")
text = input("Enter the message here : ").lower()
shift = int(input("Type the shift number : "))

def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
    return cipher_text

def decrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
    return cipher_text

if direction == "encode":
    print(encrypt(text,shift))
if direction == "decode":
    print(decrypt(text,shift))