import os

from ciphers import Vigenere
from hackers import Kasiski, Analyzer

with open('big.txt') as data_file:
    data = data_file.read()

report = open('report.md', 'w')

LANG = 'en'
VIGENERE_KEY_WORDS = [
    'AS',
    'KEY',
    'SORT',
    'FORCE',
    'SECRET',
    'COLORED',
    'ABSTRACT',
    'YESTERDAY',
    'FLYCATCHER',
    'OPPOSITIONS'
]
PERCENTS = [0.04, 0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.8, 0.9, 1]
TEXT_LENGTHS = [int(p * len(data)) for p in PERCENTS]
kasiski = Kasiski(3, LANG)
TABLE_COLS = [
    'text len',
    'keyword',
    ': len',
    'found keyword',
    ': len',
    'success probability'
]


def count_percent(keyword, founded_keyword):
    length = len(keyword)
    finded_len = len(founded_keyword)
    count = [
        (i < finded_len and founded_keyword[i] == el)
        for i, el in enumerate(keyword)
    ].count(True)
    return '{}%'.format(int(100 * count / length))


def print_table_row(*args):
    report.write('|'.join(map(str, args)))
    report.write('\n')


def print_table_head(title):
    report.write('## {}\n'.format(title))
    print_table_row(*TABLE_COLS)
    print_table_row(*['---'] * 6)


def print_test(text_len, keyword, founded_keyword):
    percent = count_percent(keyword, founded_keyword)
    print_table_row(text_len, keyword, len(keyword), founded_keyword, len(founded_keyword), percent)


def run_test(text, keyword):
    encrypted = Vigenere(keyword, LANG).encrypt(text)
    analyzer = Analyzer(kasiski.get_len(encrypted), LANG)
    finded_keyword = analyzer.find_keyword(encrypted).upper()
    print_test(len(text), keyword, finded_keyword)


def run():
    report.write('# Report\n')
    report.write('Vigenere Cipher by Ivan Pazhitnykh\n')

    print_table_head('test 1: with fixed keyword length')
    for text_len in TEXT_LENGTHS:
        run_test(data[:text_len], VIGENERE_KEY_WORDS[6])

    print_table_head('test 2: with fixed text length')
    for keyword in VIGENERE_KEY_WORDS:
        run_test(data[:6000], keyword)

    print('report generated in {}/report.md'.format(os.getcwd()))


if __name__ == '__main__':
    run()
