from sympy.solvers import solve
from sympy import Symbol, N


class Curve3rd:
    def __init__(self, *coefficients):
        self.A, self.B, self.C, self.D, self.E, self.F, self.G = coefficients
        #print(self.A, self.B, self.C, self.D, self.E, self.F, self.G)

    def get_values_of(self, x):
        y = Symbol("y")
        res = solve(self.A * x ** 2 +
                    3 * self.B * x ** 3 * y +
                    3 * self.C * x * y ** 2 +
                    self.D * y ** 3 +
                    3 * self.E * x ** 2 +
                    6 * self.F * x * y +
                    3 * self.G * y ** 2, y, manual=False)
        return res


if __name__ == '__main__':
    curve3rd = Curve3rd(0, 1, 0, 1, 0, 1, 1)
    for i in range(-10, 11):
        print([N(x) for x in curve3rd.get_values_of(i)])
