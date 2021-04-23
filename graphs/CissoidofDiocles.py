from graphs.Graph import Graph


class Cissoid(Graph):
    def __init__(self, a):
        super().__init__(a)
        self.equation = "y^2 = x^3 / (2a - x)"

    def get_value(self, t):
        try:
            x = 2 * self.a / (1 + t ** 2)
            y = 2 * self.a / (t * (1 + t ** 2))
            return x, y
        except Exception as e:
            return


if __name__ == '__main__':
    f = Cissoid(5)
    print(f.get_points_from_range(-1000, 1000))