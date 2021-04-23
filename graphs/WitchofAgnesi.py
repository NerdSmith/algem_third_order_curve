from graphs.Graph import Graph


class Witch(Graph):
    def __init__(self, a):
        super().__init__(a)
        self.equation = "y = a^3 / (a^2 + x^2)"

    def get_value(self, t):
        try:
            x = t
            y = self.a ** 3 / (self.a ** 2 + t ** 2)
            return x, y
        except Exception as e:
            return


if __name__ == '__main__':
    f = Witch(5)
    print(f.get_points_from_range(-1000, 1000))