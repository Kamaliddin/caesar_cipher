alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input('What do you want to do, Encrypt or Decrypt: ').lower()
message = input('Type your message: ').lower()
shift = int(input('What is the shift: '))

def caesar(text, shift_value, cipher_direction):
    new_text = ''
    for letter in text:
        if cipher_direction == 'encrypt':
            new_text += alphabet[alphabet.index(letter) + shift_value]
        elif cipher_direction == 'decrypt':
            new_text += alphabet[alphabet.index(letter) - shift_value]
    return new_text
            
# def encrypt(text, shift):
#     new_text = ''
#     for letter in text:
#         new_text += alphabet[alphabet.index(letter) + shift]
        
#     return new_text
# def encrypt(text, shift):
#     new_text = ''
#     for letter in text:
#         new_text += alphabet[alphabet.index(letter) - shift]
        
    # return new_text

print(caesar(message, shift, direction))