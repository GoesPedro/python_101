# Map is for mapping the values of a function, returns a map object (iterable)
import math


def area(r):
    """Calculates the area of a circle with radius 'r'."""
    return math.pi * (r ** 2)


radii = [2, 3, 4, 5, 10, 12, 15]

# Ordinary way to map results:
areas = []
for radius in radii:
    areas.append(area(radius))

print(areas)

# Mapping results with map:
areas = map(area, radii)

print(areas, type(areas))
print(list(areas))

# Map with lambda function:
print(list(map(lambda r: math.pi * r ** 2, radii)))
# After printing the result of map(), memory is wiped

# Another example:
temperaturesC = [('New York', 15), ('São Paulo', 30), ('Tokyo', 10), ('Beijing', 14), ('Seoul', 12)]
temperaturesF = list(map(lambda pair: (pair[0], 9/5 * pair[1] + 32), temperaturesC))

print(temperaturesC)
print(temperaturesF)
