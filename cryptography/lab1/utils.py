def add_to_char(char, shift, alphabet_dict):
    if not alphabet_dict.get(char.lower()):
        return char

    alphabet = sorted(list(alphabet_dict.keys()))
    index = ord(char.lower()) - ord(alphabet[0]) + shift
    next_char = alphabet[index % len(alphabet)]
    return next_char.upper() if char.istitle() else next_char
