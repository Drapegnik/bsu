#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import add_to_char, WithLanguage


class Caesar(WithLanguage):
    def __init__(self, shift, lang):
        super(Caesar, self).__init__(lang)
        self.shift = shift

    @staticmethod
    def process_string(string, shift, alphabet):
        return ''.join([add_to_char(c, shift, alphabet) for c in string])

    def encrypt(self, string):
        return Caesar.process_string(string, self.shift, self.alphabet)

    def decrypt(self, string):
        return Caesar.process_string(string, -self.shift, self.alphabet)


class Vigenere(WithLanguage):
    def __init__(self, keyword, lang):
        super(Vigenere, self).__init__(lang)
        self.keyword = keyword
        self.shifts = [ord(c.lower()) - ord(self.alphabet[0]) for c in keyword]

    def process_string(self, string, sign=1):
        shifts = self.shifts
        period = len(self.keyword)
        parts = [string[i::period] for i in range(period)]
        do_caesar = Caesar.process_string

        result_parts = [do_caesar(parts[i], sign * shifts[i], self.alphabet) for i in range(period)]

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
