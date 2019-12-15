amount_values,shifter = map(int,(input().split()))
results = []

def get_cipher(words, shifter):
    cipher_word = ""
    for i in words:
        cipher_char = ord(i)
        if(cipher_char < 65):
            cipher_word += chr(cipher_char)
            continue
        elif(cipher_char-shifter < 65):
            cipher_char += 26
        cipher_char -= shifter
        cipher_word += chr(cipher_char)
        
    return cipher_word


for i in range(amount_values):
    results.append(get_cipher(input(),shifter))

print(*results)
