from ciphers import Caesar

LANG = 'ru'
CAESAR_SHIFT = 7

with open('text_{}.txt'.format(LANG)) as data_file:
    data = data_file.read()

caesar = Caesar(CAESAR_SHIFT, LANG)
encrypted = caesar.encrypt(data)
decrypted = caesar.decrypt(encrypted)

print('task 1:')
print(' data:\t{}'.format(data))
print(' encrypted:\t{}'.format(encrypted))
print(' decrypted:\t{}'.format(decrypted))
