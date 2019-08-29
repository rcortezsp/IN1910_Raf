import numpy as np

class Quadratic:
    def __init__(self,a_2,a_1,a_0):
        self.a_2 = a_2
        self.a_1 = a_1
        self.a_0 = a_0
        self.coeffs = self.a_2,self.a_1,self.a_0

    def roots(self):
        a,b,c = self.coeffs
        q = b**2 -4*a*c
        if q < 0:
            return ()
        elif q == 0:
            x1 = -b/(2*a)
<<<<<<< HEAD
            return (x1,)

        else:
            qq = np.sqrt(q)
            x_1 = (-b - qq)/(2*a)
            x_2 = (-b + qq)/(2*a)
=======
            return(x1)

        else:
            qq = np.sqrt(q)
            x_1 = (-b + qq)/(2*a)
            x_2 = (-b - qq)/(2*a)
>>>>>>> 092e5428aefe99b7d12676788d9e35b045d04cef
            return(x_1,x_2)

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

    def __add__(self,other):
        a_2 = self.a_2 + other.a_2
        a_1 = self.a_1 + other.a_1
        a_0 = self.a_0 + other.a_0
        return Quadratic(a_2,a_1,a_0)


def test_Quadratic():
    f = Quadratic(1, -2, 1)
    assert abs(f(-1) - 4) < 1e-8
    assert abs(f(0)  - 1) < 1e-8
    assert abs(f(1)  - 0) < 1e-8

test_Quadratic()

f = Quadratic(1, -2, 1)

def test_Quadratic_add():
    f = Quadratic(1, -2, 1)
    g = Quadratic(-1, 6, -3)
    h = f + g
    a2, a1, a0 = h.coeffs
    assert a2 == 0
    assert a1 == 4
    assert a0 == -2

test_Quadratic_add()

def test_Quadratic_root():
    f1 = Quadratic(2, -2, 2)
    f2 = Quadratic(1, -2, 1)
    f3 = Quadratic(1, -3, 2)
<<<<<<< HEAD
=======
    print(f2.roots())
>>>>>>> 092e5428aefe99b7d12676788d9e35b045d04cef
    assert f1.roots() == ()
    assert abs(f2.roots()[0] - 1) < 1e-8
    assert abs(f3.roots()[0] - 1) < 1e-8 and abs(f3.roots()[1] - 2) < 1e-8

test_Quadratic_root()
