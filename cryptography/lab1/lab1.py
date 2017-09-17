from ciphers import Caesar, Vigenere
from hackers import Kasiski

LANG = 'en'
CAESAR_SHIFT = 7
VIGENERE_KEY_WORD = 'KEY'

with open('text_{}.txt'.format(LANG)) as data_file:
    data = data_file.read()

caesar = Caesar(CAESAR_SHIFT, LANG)
encrypted = caesar.encrypt(data)
decrypted = caesar.decrypt(encrypted)
print('\nCaesar:')
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

kasiski = Kasiski(3, LANG)
length = kasiski.get_len(encrypted)
print('\nKasiski:')
print(' keyword len:\t{}'.format(length))
