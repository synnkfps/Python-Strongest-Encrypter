alphabet = 'abcdefghijklmnopqrstuvwxyz'

dictionary = {}
count = 0

for i in alphabet:
    dictionary[i] = '-'*(count+1)+'|'
    count += 1

# Encrypt
def encrypt(text, conversion_dict, before=None):
    if not text: return text

    before = before or str.lower
    t = before(text)

    for key, value in conversion_dict.items():
        t = t.replace(key, value)

    return t

# Decrypt
encrypted = encrypt('hello, world!', dictionary)

decrypted = []
sentence = ''

for i in encrypted:
    if '-' not in i and i not in alphabet and '|' not in i:
        sentence += i

    if i == '|':
        decrypted.append(sentence)
        sentence = ''
        continue 

    sentence += i 
print(encrypted)

for i in decrypted:
    sentence += alphabet[len(i)-1]

print(decrypted)
print(sentence)
