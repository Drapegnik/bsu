import json

from utils import add_to_char

with open('frequencies.json') as data_file:
    freq = json.load(data_file)


class Caesar:
    def __init__(self, shift, lang):
        self.shift = shift
        if not freq.get(lang):
            raise ValueError('Unsupported language {}'.format(lang))
        self.lang = lang

    def precess_string(self, string, shift):
        return ''.join([add_to_char(c, shift, freq[self.lang]) for c in string])

    def encrypt(self, string):
        return self.precess_string(string, self.shift)

    def decrypt(self, string):
        return self.precess_string(string, -self.shift)
