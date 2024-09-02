# Currently, every single letter is always encrypted with the same letter, depending on the specified offset. What if the offset were different for each letter? This algorithm is referred to as the Vigenère cipher, where the offset for each letter is determined by another text, called the key.
# all comments refer to the line of code below them

text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

# define the vigenere function, it takes 3 args (message, key, and direction which is set to 1 by default)
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    for char in message.lower():
        
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # key_char is the character in the key string at the position determined by key_index % len(key)
            # key_index % len(key) ensures that the key is used cyclically. For example, if key is 'python' and key_index is 7, key_index % len(key) equals 1 (since 7 % 6 = 1), thus selecting the second character of key.
            key_char = key[key_index % len(key)]

            # key_index keeps track of the position in the key
            key_index += 1
            
            # position of key_char in the alphabet string
            offset = alphabet.index(key_char)
            
            # find the index of the character(char) in the message via the alphabet string
            # example: the message is hello, the first value for index would be 7 because h is indexed at 7 in the alphabet string
            index = alphabet.find(char)
            
            # the new index (i.e., how much we're shifting the letters by) is set to the original index of the char + offset
            new_index = (index + offset*direction) % len(alphabet)
            
            final_message += alphabet[new_index]
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')