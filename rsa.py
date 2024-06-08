import math
import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Често използвано публично експоненциално число
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(2, phi)
        g = gcd(e, phi)
    d = find_mod_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt_rsa(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]


def decrypt_rsa(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])



p = 61  
q = 53 
public_key, private_key = generate_keypair(p, q)

# test
message = "Hello"
ciphertext = encrypt_rsa(public_key, message)
plaintext = decrypt_rsa(private_key, ciphertext)

assert plaintext == message
