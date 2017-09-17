import re

from utils import WithLanguage, is_all_letters, list_gcd


class Kasiski(WithLanguage):
    def __init__(self, length, lang):
        super(Kasiski, self).__init__(lang)
        self.l = length

    def get_pattern(self, substr):
        return '(?={})'.format(substr)

    def get_gramms(self, string):
        gramms = {}
        for i in range(len(string) - self.l):
            substr = string[i:i + self.l]
            if not is_all_letters(substr, self.lang):
                continue
            if gramms.get(substr):
                continue
            matches = [m.start() for m in re.finditer(self.get_pattern(substr), string)]
            if len(matches) > 1:
                gramms[substr] = matches
        return gramms

    def get_differencies(self, array):
        diffs = {}
        for el in array:
            for i in range(len(el) - 1):
                key = el[i + 1] - el[i]
                diffs[key] = diffs.get(key, 0) + 1
        return [key for key in diffs if diffs[key] > 1]

    def get_len(self, encrypted):
        gramms = self.get_gramms(encrypted.lower())
        diffs = self.get_differencies(list(gramms.values()))
        gcd = list_gcd(diffs)
        return gcd
