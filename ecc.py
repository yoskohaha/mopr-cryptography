import random
import math

class EllipticCurve:

    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, x, y):
        return (y**2 - x**3 - self.a * x - self.b) % self.p == 0

    def point_addition(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P

        x1, y1 = P
        x2, y2 = Q

        if (x1, y1) == (x2, -y2 % self.p):
            return None

        if P != Q:
            m = (y2 - y1) * pow(x2 - x1, -1, self.p) % self.p
        else:
            m = (3 * x1 * x1 + self.a) * pow(2 * y1, -1, self.p) % self.p

        x3 = (m * m - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def point_multiplication(self, k, P):
        R = None
        N = P

        while k:
            if k & 1:
                R = self.point_addition(R, N)
            N = self.point_addition(N, N)
            k >>= 1

        return R