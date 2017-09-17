import json

from utils import add_to_char

with open('frequencies.json') as data_file:
    freq = json.load(data_file)


class WithLanguage:
    def __init__(self, lang):
        if not freq.get(lang):
            raise ValueError('Unsupported language {}'.format(lang))
        self.lang = lang


class Caesar(WithLanguage):
    def __init__(self, shift, lang):
        super(Caesar, self).__init__(lang)
        self.shift = shift

    @staticmethod
    def process_string(string, shift, lang):
        return ''.join([add_to_char(c, shift, freq[lang]) for c in string])

    def encrypt(self, string):
        return Caesar.process_string(string, self.shift, self.lang)

    def decrypt(self, string):
        return Caesar.process_string(string, -self.shift, self.lang)


class Vigenere(WithLanguage):
    def __init__(self, keyword, lang):
        super(Vigenere, self).__init__(lang)
        self.keyword = keyword
        alphabet = sorted(list(freq[lang].keys()))
        self.shifts = [ord(c.lower()) - ord(alphabet[0]) for c in keyword]
        self.lang = lang

    def process_string(self, string, sign=1):
        shifts = self.shifts
        lang = self.lang
        period = len(self.keyword)
        parts = [string[i::period] for i in range(period)]
        do_caesar = Caesar.process_string

        result_parts = [do_caesar(parts[i], sign * shifts[i], lang) for i in range(period)]

        letters = []
        for j in range(len(result_parts[0])):
            for i in range(period):
                if j < len(result_parts[i]):
                    letters.append(result_parts[i][j])

        return ''.join(letters)

    def encrypt(self, string):
        return self.process_string(string)

    def decrypt(self, string):
        return self.process_string(string, -1)


