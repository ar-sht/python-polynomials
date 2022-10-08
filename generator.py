import numpy as np

import polynomial
import quadratic


def flatten(l):
    return [item for sublist in l for item in sublist]


# creates a quadratic from three points using magic matrices
class Generator:
    def __init__(self, *points):
        self.points = points
        self.x_coords = []
        self.y_coords = []
        for point in self.points:
            self.x_coords.append(point[0])
            self.y_coords.append(point[1])
        self.equation = None

    def generate_equation(self):
        if len(self.points) < 3:
            print(f"Equation cannot be generated with so few points (#{len(self.points)}), please enter at least 3.")
            return
        elif len(self.points) == 3:
            solutions = self.create_polynomial()
            a = solutions[0, 0]
            b = solutions[1, 0]
            c = solutions[2, 0]
            self.equation = quadratic.Quadratic(a, b, c)
        else:
            solutions = flatten(self.create_polynomial().tolist())
            print(solutions)
            self.equation = polynomial.Polynomial(solutions)

    def create_polynomial(self):
        input_array = []
        degree = len(self.x_coords)
        for point in self.x_coords:
            added_array = []
            for i in range(1, degree + 1):
                added_array.append(point ** (degree - i))
            input_array.append(added_array)

        output_array = []
        for point in self.y_coords:
            output_array.append([point])

        input_matrix = np.matrix(input_array)
        output_matrix = np.matrix(output_array)
        solutions_matrix = np.matmul(input_matrix.getI(), output_matrix)
        return solutions_matrix
