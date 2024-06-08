import unittest
from ecc import EllipticCurve

class TestEllipticCurve(unittest.TestCase):
    def setUp(self):
        self.curve = EllipticCurve(2, 2, 17)
        self.G = (5, 1)

    def test_is_on_curve(self):
        self.assertTrue(self.curve.is_on_curve(5, 1))
        self.assertFalse(self.curve.is_on_curve(5, 2))

    def test_point_addition(self):
        P = (5, 1)
        Q = (6, 3)
        R = self.curve.point_addition(P, Q)
        self.assertEqual(R, (10, 6))

    def test_point_addition_with_neutral_element(self):
        P = (5, 1)
        O = None
        R = self.curve.point_addition(P, O)
        self.assertEqual(R, P)

    def test_point_addition_with_inverse(self):
        P = (5, 1)
        Q = (5, 16)  # (5, -1 mod 17)
        R = self.curve.point_addition(P, Q)
        self.assertIsNone(R)

    def test_point_multiplication(self):
        k = 2
        R = self.curve.point_multiplication(k, self.G)
        self.assertEqual(R, (6, 3))

    def test_point_multiplication_zero(self):
        k = 0
        R = self.curve.point_multiplication(k, self.G)
        self.assertIsNone(R)

    def test_point_multiplication_one(self):
        k = 1
        R = self.curve.point_multiplication(k, self.G)
        self.assertEqual(R, self.G)

if __name__ == '__main__':
    unittest.main()
