import unittest
from defie_hellman import generate_private_key, calculate_public_key, calculate_shared_secret

class TestDiffieHellman(unittest.TestCase):
    def setUp(self):
        self.p = 23  # Малко просто число за лесно тестване
        self.g = 5
        self.private_key_A = generate_private_key(self.p)
        self.private_key_B = generate_private_key(self.p)
        self.public_key_A = calculate_public_key(self.g, self.private_key_A, self.p)
        self.public_key_B = calculate_public_key(self.g, self.private_key_B, self.p)

    def test_key_exchange(self):
        shared_secret_A = calculate_shared_secret(self.public_key_B, self.private_key_A, self.p)
        shared_secret_B = calculate_shared_secret(self.public_key_A, self.private_key_B, self.p)
        self.assertEqual(shared_secret_A, shared_secret_B)

if __name__ == '__main__':
    unittest.main()
