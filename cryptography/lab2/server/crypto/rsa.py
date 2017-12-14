import random
from math import gcd


def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for n in range(3, int(x ** 0.5) + 2, 2):
        if x % n == 0:
            return False
    return True


def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative inverse of two numbers
    """
    d, next_d, temp_phi = 0, 1, phi
    while e > 0:
        quotient = temp_phi // e
        d, next_d = next_d, d - quotient * next_d
        temp_phi, e = e, temp_phi - quotient * e
    if temp_phi > 1:
        raise ValueError('e is not invertible by modulo phi.')
    if d < 0:
        d += phi
    return d


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime!')
    elif p == q:
        raise ValueError('P and Q cannot be equal!')
    n = p * q
    e = 0
    phi = (p - 1) * (q - 1)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(public_key, text):
    """
    :param public_key: (e, n)
    :param text: text to encrypt
    :return: list of encrypted bytes
    """
    e, n = public_key
    encrypted = [pow(ord(x), e, n) for x in text]
    return encrypted


def decrypt(private_key, encrypted):
    """
    :param private_key: (d, n)
    :param encrypted: list of encrypted bytes
    :return: decrypted string
    """
    d, n = private_key
    plain = [chr(int(pow(x, d, n))) for x in encrypted]
    return ''.join(plain)
