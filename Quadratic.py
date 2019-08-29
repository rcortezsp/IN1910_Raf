import numpy as np
class Quadratic:
    def __init__(self,a_2,a_1,a_0):
        self.a_2 = a_2
        self.a_1 = a_1
        self.a_0 = a_0
class Quadratic(Quadratic):
    def __call__(self,x):
        return self.a_2 * x**2 + self.a_1 *x + self.a_0
