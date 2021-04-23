from graphs.Graph import Graph


class Folium(Graph):
    def __init__(self, a):
        super().__init__(a)
        self.equation = "x^3 + y^3 - 3axy = 0"

    def get_value(self, t):
        try:
            x = (3 * self.a * t) / (1 + t ** 3)
            y = (3 * self.a * t ** 2) / (1 + t ** 3)
            return x, y
        except Exception as e:
            return


if __name__ == '__main__':
    f = Folium(5)
    print(f.get_points_from_range(-1000, 1000))
