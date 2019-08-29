import numpy as np

class Quadratic:
    def __init__(self,a_2,a_1,a_0):
        self.a_2 = a_2
        self.a_1 = a_1
        self.a_0 = a_0


class Quadratic(Quadratic):
    def __call__(self,x):
        return self.a_2 * x**2 + self.a_1 *x + self.a_0

    def __str__(self):
        if self.a_1 < 0 :
            fortegn = "-"
        elif self.a_1 >= 0:
            fortegn = "+"
        if self.a_0 < 0 :
            fortegn_2 = "-"
        elif self.a_0 >= 0:
            fortegn_2 = "+"
        return f"{self.a_2}x^2 {fortegn} {abs(self.a_1)}x {fortegn_2} {abs(self.a_0)}"

def test_Quadratic():
    f = Quadratic(1, -2, 1)
    assert abs(f(-1) - 4) < 1e-8
    assert abs(f(0)  - 1) < 1e-8
    assert abs(f(1)  - 0) < 1e-8

test_Quadratic()
"""
f = Quadratic(1, -2, 1)
print(f)
"""
