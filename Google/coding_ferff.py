ciphertext = "Eqfkpi vguvu ctg hwp!"
knownword = "tests"

cipher = ciphertext.split(" ");
ans = ""


def encrypt_string(input_string, k):
    encrypted = ""
    for char in input_string:
        # Encrypt uppercase letters
        if char.isalpha() and char.isupper():
            encrypted += chr((ord(char) + k - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.isalpha() and char.islower():
            encrypted += chr((ord(char) + k - 97) % 26 + 97)
        # Encrypt 'a' to 'z'
        elif char.isalpha() and char.lower() == 'a':
            encrypted += 'z' if char.islower() else 'Z'
        # Encrypt other characters unchanged
        else:
            encrypted += char
    return encrypted


shift = []
for i in range(0,len(cipher)):
    word = cipher[i]
    
    if len(word) != len(knownword):
        continue
        
        
    diff = set()
    for j in range(0,len(word)):
        diff.add(ord(word[j])- ord(knownword[j]))
        
    #check if we found somwthing
    if len(diff) == 1:
        shift = [i for i in diff]
        
        
if not shift:
    print("invalid")
else:
    print(encrypt_string(ciphertext , -shift[0]))
    
    
        
    