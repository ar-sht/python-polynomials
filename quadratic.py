from polynomial import Polynomial

class Quadratic(Polynomial):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        self.a = a
        self.b = b
        self.c = c

    def get_roots(self):
        discriminant = (self.b ** 2) - (4 * self.a * self.c)
        root1 = (-1 * self.b + discriminant ** (1 / 2)) / (2 * self.a)
        root2 = (-1 * self.b + discriminant ** (1 / 2)) / (2 * self.a)
        return [root1, root2]

    def get_vertex(self):
        x_value = (-1 * self.b) / (2 * self.a)
        y_value = self.evaluate(x_value)
        return [x_value, y_value]
