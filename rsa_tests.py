import unittest
from rsa import *

class TestRSA(unittest.TestCase):
    def setUp(self):
        self.p = 61  
        self.q = 53
        self.public_key, self.private_key = generate_keypair(self.p, self.q)
        self.message = "Test"

    def test_key_generation(self):
        e, n = self.public_key
        d, n2 = self.private_key
        self.assertEqual(n, n2)
        self.assertTrue(e > 1 and e < (self.p - 1) * (self.q - 1))
        self.assertTrue(d > 1 and d < (self.p - 1) * (self.q - 1))

    def test_rsa_encryption_decryption(self):
        ciphertext = encrypt_rsa(self.public_key, self.message)
        plaintext = decrypt_rsa(self.private_key, ciphertext)
        self.assertEqual(plaintext, self.message)