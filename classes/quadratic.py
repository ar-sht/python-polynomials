from classes.polynomial import Polynomial

class Quadratic(Polynomial):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        self.a = round(a, 2)
        self.b = round(b, 2)
        self.c = round(c, 2)

    def get_roots(self):
        discriminant = (self.b ** 2) - (4 * self.a * self.c)
        root1 = (-1 * self.b + discriminant ** (1 / 2)) / (2 * self.a)
        root2 = (-1 * self.b - discriminant ** (1 / 2)) / (2 * self.a)
        if type(root1) is complex or type(root2) is complex:
            root1 = complex(round(root1.real, 2), round(root1.imag, 2))
            root2 = complex(round(root2.real, 2), round(root2.imag, 2))
        else:
            root1 = round(root1, 2)
            root2 = round(root2, 2)

        return [root1, root2]

    def get_vertex(self):
        x_value = (-1 * self.b) / (2 * self.a)
        y_value = self.evaluate(x_value)
        return [round(x_value, 2), round(y_value, 2)]
