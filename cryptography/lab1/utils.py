#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
from functools import reduce
from math import gcd

LETTERS_REGEXPS = {
    'en': re.compile('^[a-zA-Z]+$'),
    'ru': re.compile('^[а-яА-Я]+$')
}

with open('frequencies.json') as data_file:
    frequencies = json.load(data_file)


class WithLanguage:
    def __init__(self, lang):
        freq = frequencies.get(lang)
        if not freq:
            raise ValueError('Unsupported language {}'.format(lang))
        self.lang = lang
        self.known_freq = freq_to_sorted_list(freq)
        self.alphabet = sorted(list(freq.keys()))


def add_to_char(char, shift, alphabet):
    if char.lower() not in alphabet:
        return char

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


def freq_to_sorted_list(dict):
    return sorted([{'letter': k, 'freq': v} for k, v in dict.items()], key=lambda x: x['freq'], reverse=True)
