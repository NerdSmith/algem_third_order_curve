
class Graph:
    def __init__(self, a):
        self.a = a

    def get_value(self, t):
        return self.a, self.a

    def get_points_from_range(self, from_, to):
        points = []
        for i in range(from_, to + 1):
            i /= 10
            x_y = self.get_value(i)
            if x_y is not None:
                for j in x_y:
                    points.append(j)

        return points