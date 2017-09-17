import json
import re
from functools import reduce
from math import gcd

LETTERS_REGEXPS = {
    'en': re.compile('^[a-zA-Z]+$'),
    'ru': re.compile('^[а-яА-Я]+$')
}

with open('frequencies.json') as data_file:
    freq = json.load(data_file)


class WithLanguage:
    def __init__(self, lang):
        if not freq.get(lang):
            raise ValueError('Unsupported language {}'.format(lang))
        self.lang = lang


def add_to_char(char, shift, alphabet_dict):
    if not alphabet_dict.get(char.lower()):
        return char

    alphabet = sorted(list(alphabet_dict.keys()))
    index = ord(char.lower()) - ord(alphabet[0]) + shift
    next_char = alphabet[index % len(alphabet)]
    return next_char.upper() if char.istitle() else next_char


def is_all_letters(string, lang):
    pattern = LETTERS_REGEXPS.get(lang)
    if not pattern:
        raise ValueError('Unsupported language {}'.format(lang))
    return bool(pattern.match(string))


def list_gcd(list):
    return reduce(gcd, list)
