import numpy as np
import matplotlib.pyplot as plt

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
            return (x1,)

        else:
            qq = np.sqrt(q)
            x_1 = (-b - qq)/(2*a)
            x_2 = (-b + qq)/(2*a)
            return(x_1,x_2)

    def intersection(self,other):
        a_f,b_f,c_f = self.coeffs
        a_g,b_g,c_g = other.coeffs
        f_i = Quadratic(a_f,b_f,c_f)
        g_i = Quadratic(a_g,b_g,c_g)
        h = f_i - g_i
        r = h.roots()
        return ((r[0],f_i(r[0])),(r[1],f_i(r[1])))


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

    def __sub__(self,other):
        a_2 = self.a_2 - other.a_2
        a_1 = self.a_1 - other.a_1
        a_0 = self.a_0 - other.a_0
        return Quadratic(a_2,a_1,a_0)


if __name__ == "__main__":
    def test_Quadratic():
        f = Quadratic(1, -2, 1)
        assert abs(f(-1) - 4) < 1e-8
        assert abs(f(0)  - 1) < 1e-8
        assert abs(f(1)  - 0) < 1e-8



    def test_Quadratic_add():
        f = Quadratic(1, -2, 1)
        g = Quadratic(-1, 6, -3)
        h = f + g
        a2, a1, a0 = h.coeffs
        assert a2 == 0
        assert a1 == 4
        assert a0 == -2


    def test_Quadratic_root():
        f1 = Quadratic(2, -2, 2)
        f2 = Quadratic(1, -2, 1)
        f3 = Quadratic(1, -3, 2)
        assert f1.roots() == ()
        assert abs(f2.roots()[0] - 1) < 1e-8
        assert abs(f3.roots()[0] - 1) < 1e-8 and abs(f3.roots()[1] - 2) < 1e-8


    def test_Quadratic_intersection():
        f = Quadratic(1,-2,1)
        g = Quadratic(2,3,-2)
        inter = f.intersection(g)
        assert abs(inter[0][0] - 0.5414) < 1e-3 and abs(inter[0][1] - 0.2103) < 1e-3
        assert abs(inter[1][0] - (-5.541)) < 1e-3 and abs(inter[1][1] - 42.79) < 1e-3
        x = np.linspace(-7, 4, 1000)
        plt.xlim(-6,3)
        plt.ylim(-3,45)
        plt.plot(x, f(x),label = f'$f(x)$')
        plt.plot(x, g(x),label = f'$g(x)$')
        plt.plot(inter[0][0],inter[0][1],"o", label= 'intersection point 1')
        plt.plot(inter[1][0],inter[1][1],"o", label= 'intersection point 2')
        plt.grid()
        plt.legend()
        plt.show()


    test_Quadratic()
    test_Quadratic_add()
    test_Quadratic_root()
    test_Quadratic_intersection()
