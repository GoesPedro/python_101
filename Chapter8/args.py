# *args is a parameter like any other, and can be named differently, but keeping the asterisk
# *args is used to allow multiple values to be passed as arguments
# these arguments will be gathered as a tuple


def add(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add(12, 13))

# Simple asterisk indicates a collection of data (except dictionaries) to be unpacked:
numbers = [42, 31, 5.53, 91, -3, 5]
print(add(*numbers))
