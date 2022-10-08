class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self, value):
        first_term = self.a * (value ** 2)
        second_term = self.b * value
        third_term = self.c
        return first_term + second_term + third_term

    def get_roots(self):
        discriminant = (self.b ** 2) - (4 * self.a * self.c)
        root1 = (-1 * self.b + discriminant ** (1 / 2)) / (2 * self.a)
        root2 = (-1 * self.b + discriminant ** (1 / 2)) / (2 * self.a)
        return [root1, root2]

    def get_vertex(self):
        x_value = (-1 * self.b) / (2 * self.a)
        y_value = self.evaluate(x_value)
        return [x_value, y_value]
