class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = []
        for coefficient in coefficients:
            self.coefficients.append(round(coefficient, 2))
        self.degree = len(coefficients) - 1
        self.roots = []

    def evaluate(self, value):
        total = 0
        degree = self.degree
        for coefficient in self.coefficients:
            total += value ** degree * coefficient
            degree -= 1
        return total

    def pretty_print(self):
        output_string = ""
        degree = self.degree
        for coefficient in self.coefficients:
            if coefficient < 0:
                output_string += "- "
            elif coefficient > 0 and degree != self.degree:
                output_string += '+ '
            if coefficient != 0:
                if coefficient != 1:
                    output_string += str(abs(coefficient))
                if degree > 0:
                    output_string += "x"
                    if degree > 1:
                        output_string += f"^{degree}"
                output_string += " "
            degree -= 1

        return output_string
