from ciphers import Caesar, Vigenere, Kasiski

LANG = 'en'
CAESAR_SHIFT = 7
VIGENERE_KEY_WORD = 'KEY'

with open('text_{}.txt'.format(LANG)) as data_file:
    data = data_file.read()

caesar = Caesar(CAESAR_SHIFT, LANG)
encrypted = caesar.encrypt(data)
decrypted = caesar.decrypt(encrypted)
print(' data:\t\t{}'.format(data))
print(' encrypted:\t{}'.format(encrypted))
print(' decrypted:\t{}'.format(decrypted))
print('-' * 100)

vigenere = Vigenere(VIGENERE_KEY_WORD, LANG)
encrypted = vigenere.encrypt(data)
decrypted = vigenere.decrypt(encrypted)
print('\nVigenere:')
print(' data:\t\t{}'.format(data))
print(' encrypted:\t{}'.format(encrypted))
print(' decrypted:\t{}'.format(decrypted))
print('-' * 100)

