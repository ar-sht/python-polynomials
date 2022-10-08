class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.degree = len(coefficients) - 1
        self.roots = []

    def evaluate(self, value):
        total = 0
        degree = self.degree
        for coefficient in self.coefficients:
            total += value ** degree * coefficient
            degree -= 1
        return total
