import re
from math import ceil

from utils import WithLanguage, is_all_letters, list_gcd, freq_to_sorted_list, add_to_char

DIFF_THRESHOLD = 0.1


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
        common_diff = diffs[max(diffs, key=lambda k: diffs[k])]
        min_accepted_diff = ceil(common_diff * DIFF_THRESHOLD)
        return [key for key in diffs if diffs[key] > min_accepted_diff]

    def get_len(self, encrypted):
        gramms = self.get_gramms(encrypted.lower())
        diffs = self.get_differencies(list(gramms.values()))
        gcd = list_gcd(diffs)
        return gcd


class Analyzer(WithLanguage):
    def __init__(self, length, lang):
        super(Analyzer, self).__init__(lang)
        self.length = length

    @staticmethod
    def count_frequencies(string, alphabet):
        letters_count = dict.fromkeys(alphabet, 0)
        escaped = 0
        for c in string:
            if letters_count.get(c.lower()) is not None:
                letters_count[c.lower()] += 1
            else:
                escaped += 1
        string_len = len(string) - escaped
        return {letter: count / string_len for letter, count in letters_count.items()}

    def next_freq_closer(self, value, known_freq):
        return abs(value - known_freq[0]['freq']) > abs(value - known_freq[1]['freq'])

    def count_shift(self, a, b):
        return ord(a['letter']) - ord(b['letter'])

    def find_keyword_letter(self, string):
        shifts = {}
        known_freq = self.known_freq[:]
        freq = freq_to_sorted_list(Analyzer.count_frequencies(string, self.alphabet))
        for el in freq:
            i = 0
            while i < len(known_freq) - 1:
                closest = known_freq[i]
                if not self.next_freq_closer(el['freq'], known_freq[i:]):
                    break
                i += 1
            shift = self.count_shift(el, closest)
            shifts[shift] = shifts.get(shift, 0) + 1
        common_shift = max(shifts, key=lambda k: shifts[k])
        # common_shift = self.count_shift(freq[0], known_freq[0])  # diff between most popular
        return add_to_char(self.alphabet[0], common_shift, self.alphabet)

    def find_keyword(self, string):
        parts = [string[i::self.length] for i in range(self.length)]
        letters = list(map(self.find_keyword_letter, parts))
        return ''.join(letters)
