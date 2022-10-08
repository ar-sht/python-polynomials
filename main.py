import classes.quadratic
import classes.grapher
import classes.generator
import re


def num_input(prompt):
    value = input(prompt)
    while not re.match(r"-?\d*", value):
        value = input("Invalid input. Please try again:\n")
    return value


def point_input(prompt):
    point = input(prompt)
    while not re.match(r"-?\d*\s-?\d*", point) and point != "done":
        point = input("Invalid input. Please try again:\n")
    return point


print("Welcome to polynomial things!")
print("1. Enter a quadratic and learn stuff about it")
print("2. Enter 3 or more points and see the graph & equation")
choice1 = input("What would you like to do?\n")
while not re.match(r"[12]", choice1):
    choice1 = input("Invalid input. Please try again: ")

if int(choice1) == 1:
    print("Enter the coefficients of your quadratic in the standard form ax^2 + bx + c:")
    a = int(num_input("a: "))
    b = int(num_input("b: "))
    c = int(num_input("c: "))

    given_polynomial = classes.quadratic.Quadratic(a, b, c)

    print(f"The quadratic you entered is {given_polynomial.pretty_print()}")
else:
    points = []
    point = None
    i = 1
    print("When entering points use the format 'x y', be sure to leave a space in between!")
    print("Enter 'done' if you're done entering points.")
    while True:
        point = point_input(f"Enter point #{i}: ")
        if point == "done":
            break
        point_array = []
        for val in point.split(" "):
            point_array.append(int(val))
        points.append(point_array)
        i += 1

    nice_points = []
    for point in points:
        x = point[0]
        y = point[1]
        nice_points.append(f"({x}, {y})")

    print(f"The points you entered were {', '.join(nice_points)}")

    generator = classes.generator.Generator(points)
    generator.generate_equation()
    given_polynomial = generator.equation

    print(f"The polynomial that fits those points is {given_polynomial.pretty_print()}")

if type(given_polynomial) is classes.quadratic.Quadratic:
    roots = given_polynomial.get_roots()
    string_roots = []
    for root in roots:
        string_roots.append(f"(0, {root})")

    vertex = given_polynomial.get_vertex()
    string_vertex = []
    for coordinate in vertex:
        string_vertex.append(str(coordinate))

    print(f"The roots of this quadratic are {', and '.join(string_roots)}")
    print(f"The vertex is ({', '.join(string_vertex)})")

graph = input("Would you like to see the graph? (y/n)\n")
if graph[0].lower() == "y":
    minimum = int(num_input("What would you like the minimum bound to be?\n"))
    maximum = int(num_input("What would you like the maximum bound to be?\n"))

    grapher = classes.grapher.Grapher(given_polynomial)
    grapher.generate_points(minimum, maximum)
    grapher.graph()
else:
    print("Ok then. Bye bye!")
