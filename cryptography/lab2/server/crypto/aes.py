"""
Advanced Encryption Standard aka Rijndael algorithm
http://en.wikipedia.org/wiki/Advanced_Encryption_Standard
"""
from crypto.constants import SBOX, INV_SBOX, RCON
from crypto.utils import mul_by_02, mul_by_03, mul_by_09, mul_by_0b, mul_by_0d, mul_by_0e, state_to_list

ROWS_NUM = 4
COLS_NUM = 4
KEY_LENGTH = ROWS_NUM * COLS_NUM
ROUNDS_NUM = 10


def sub_bytes(state, inv=False):
    """
    Replace every element from state on element from SBOX / INV_SBOX
    like state[k] = SBOX[i][j], where i, j from hex(state[k]) == '0x{i}{j}'
        :param state: array of [ROWS_NUMxCOLS_NUM] size
        :param inv: True - decrypt, False - encrypt
        :return: new state
    """
    new_state = state[:]
    box = INV_SBOX if inv else SBOX
    for i, row in enumerate(new_state):
        for j, el in enumerate(row):
            b_i = el // 0x10
            b_j = el % 0x10
            new_state[i][j] = box[16 * b_i + b_j]  # box is flat list
    return new_state


def shift_rows(state, inv=False):
    """
    Shift rows of state:
     - fourth row over 3 bytes
     - third row over 2 bytes
     - second row over 1 byte
     - first row not changed
    
        :param state: array of [ROWS_NUMxCOLS_NUM] size
        :param inv: True - decrypt (right shift), False - encrypt (left shift)
        :return: new state
    """
    new_state = state[:]
    for i in range(1, ROWS_NUM):
        sign = -1 if inv else 1
        new_state[i] = new_state[i][sign * i:] + new_state[i][:sign * i]
    return new_state


def mix_columns(state, inv=False):
    """
    Multiply every column of state by polynomial:
     - for decrypt by a'(x) = {0b}x**3 + {0d}x**2 + {09}x + {0e}
     - for encrypt by a(x) = {03}x**3 + {01}x**2 + {01}x + {02}
        :param state: array of [ROWS_NUMxCOLS_NUM] size
        :param inv: True - decrypt, False - encrypt
        :return: new state
    """
    new_state = state[:]
    for i in range(ROWS_NUM):
        if inv:  # decryption
            s0 = mul_by_0e(state[0][i]) ^ mul_by_0b(state[1][i]) ^ mul_by_0d(state[2][i]) ^ mul_by_09(state[3][i])
            s1 = mul_by_09(state[0][i]) ^ mul_by_0e(state[1][i]) ^ mul_by_0b(state[2][i]) ^ mul_by_0d(state[3][i])
            s2 = mul_by_0d(state[0][i]) ^ mul_by_09(state[1][i]) ^ mul_by_0e(state[2][i]) ^ mul_by_0b(state[3][i])
            s3 = mul_by_0b(state[0][i]) ^ mul_by_0d(state[1][i]) ^ mul_by_09(state[2][i]) ^ mul_by_0e(state[3][i])
        else:  # encryption
            s0 = mul_by_02(state[0][i]) ^ mul_by_03(state[1][i]) ^ state[2][i] ^ state[3][i]
            s1 = state[0][i] ^ mul_by_02(state[1][i]) ^ mul_by_03(state[2][i]) ^ state[3][i]
            s2 = state[0][i] ^ state[1][i] ^ mul_by_02(state[2][i]) ^ mul_by_03(state[3][i])
            s3 = mul_by_03(state[0][i]) ^ state[1][i] ^ state[2][i] ^ mul_by_02(state[3][i])
        new_state[0][i] = s0
        new_state[1][i] = s1
        new_state[2][i] = s2
        new_state[3][i] = s3
    return new_state


def get_round_key(key):
    """
    Generate list of round keys
        :param key: algorithm key, string of KEY_LENGTH size
        :return: array of [ROWS_NUMxCOLS_NUM] size
    """
    key_symbols = [ord(symbol) for symbol in key]
    key_schedule = [
        [key_symbols[i + ROWS_NUM * j] for j in range(COLS_NUM)]
        for i in range(ROWS_NUM)
    ]

    for j in range(ROWS_NUM, COLS_NUM * (ROUNDS_NUM + 1)):
        if j % ROWS_NUM == 0:
            temp = [key_schedule[i][j - 1] for i in range(1, ROWS_NUM)]
            temp.append(key_schedule[0][j - 1])

            for i in range(ROWS_NUM):
                sbox_i = temp[i] // 0x10
                sbox_j = temp[i] % 0x10
                temp[i] = SBOX[16 * sbox_i + sbox_j]

            for i in range(ROWS_NUM):
                s = (key_schedule[i][j - COLS_NUM]) ^ (temp[i]) ^ (RCON[i][int(j / ROWS_NUM - 1)])
                key_schedule[i].append(s)
        else:
            for i in range(ROWS_NUM):
                s = key_schedule[i][j - COLS_NUM] ^ key_schedule[i][j - 1]
                key_schedule[i].append(s)
    return key_schedule


def add_round_key(state, round_key, round_num=0):
    """
    Perform XOR of state and round_key
        :param state: array of [ROWS_NUMxCOLS_NUM] size
        :param round_key: array of [ROWS_NUMxCOLS_NUM] size, see get_round_key()
        :param round_num: number of crypt round
        :return: new_state
    """
    new_state = state[:]
    for i in range(ROWS_NUM):
        for j in range(COLS_NUM):
            new_state[i][j] = new_state[i][j] ^ round_key[i][COLS_NUM * round_num + j]
    return new_state


def process(input_bytes, key, method):
    bad_symbols = list(filter(lambda s: ord(s) > 255, key))
    if len(key) != KEY_LENGTH or bad_symbols:
        raise ValueError('Key should be length {} and contain only latin alphabet and numbers'.format(KEY_LENGTH))
    round_key = get_round_key(key)
    processed = []
    for i in range(0, len(input_bytes), KEY_LENGTH):
        chunk = input_bytes[i:i + KEY_LENGTH]
        if len(chunk) < KEY_LENGTH:  # supplement to full chunk
            chunk.extend([0] * (KEY_LENGTH - len(chunk) - 1))
            chunk.append(1)
        processed.extend(method(chunk, round_key))
    return processed


def encrypt(input_bytes, key):
    """
    :param input_bytes: data as list of bytes
    :param key: string on KEY_LENGTH size
    :return: encrypted data as list of int's
    """
    return process(input_bytes, key, encrypt_chunk)


def encrypt_chunk(input_chunk, round_key):
    """
    :param input_chunk: list of bytes [ROWS_NUM, COLS_NUM] size
    :round_key see get_round_key()
    :return: encrypted chunk data as list of int's
    """
    state = [[input_chunk[i + ROWS_NUM * j] for j in range(COLS_NUM)] for i in range(ROWS_NUM)]
    state = add_round_key(state, round_key)

    for round_num in range(1, ROUNDS_NUM):
        state = add_round_key(mix_columns(shift_rows(sub_bytes(state))), round_key, round_num)
    state = add_round_key(shift_rows(sub_bytes(state)), round_key, ROUNDS_NUM)
    return state_to_list(state)


def decrypt(input_bytes, key):
    """
    :param input_bytes: data as list of bytes
    :param key: string on KEY_LENGTH size
    :return: decrypted data as list of int's
    """
    return process(input_bytes, key, decrypt_chunk)


def decrypt_chunk(input_chunk, round_key):
    """
    :param input_chunk: list of bytes [ROWS_NUM, COLS_NUM] size
    :round_key see get_round_key()
    :return: decrypted chunk data as list of int's
    """
    state = [[input_chunk[i + ROWS_NUM * j] for j in range(COLS_NUM)] for i in range(ROWS_NUM)]
    state = add_round_key(state, round_key, ROUNDS_NUM)
    for round_num in range(ROUNDS_NUM - 1, 0, -1):
        state = mix_columns(add_round_key(sub_bytes(shift_rows(state, True), True), round_key, round_num), True)
    state = add_round_key(sub_bytes(shift_rows(state, True), True), round_key, 0)
    return state_to_list(state)
