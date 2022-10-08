import quadratic
import matplotlib.pyplot as plt

from quadratic import Quadratic
from polynomial import Polynomial
from generator import Generator


class Grapher:
    def __init__(self, equation: Polynomial):
        self.equation = equation
        self.x_values = []
        self.y_values = []

    def generate_points(self, minimum=-10, maximum=10):
        for i in range(minimum, maximum + 1):
            self.x_values.append(i)
            self.y_values.append(self.equation.evaluate(i))

    def graph(self):
        plt.plot(self.x_values, self.y_values, scalex=self.x_values[-1] - self.x_values[0],
                 scaley=max(self.y_values) - min(self.y_values), marker='.')
        plt.show()
