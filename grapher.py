import quadratic
import numpy as np
import matplotlib.pyplot as plt

from quadratic import Quadratic


class Grapher:
    def __init__(self, equation: Quadratic):
        self.equation = equation
        self.x_values = []
        self.y_values = []

    def generate_points(self, minimum=-10, maximum=10):
        for i in range(minimum, maximum + 1):
            self.x_values.append(i)
            self.y_values.append(self.equation.evaluate(i))

    def graph(self):
        plt.plot(self.x_values, self.y_values, scalex=self.x_values[-1] - self.x_values[0],
                 scaley=self.y_values[-1] - self.y_values[0], marker='.')
        plt.show()


test_equation: Quadratic = quadratic.Quadratic(1, -1, -2)
tester = Grapher(test_equation)
tester.generate_points(-100, 100)
tester.graph()
