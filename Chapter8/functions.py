# Defining a function:
def congrats_name_score(name, score):
    print(f'Congratulations, {name}!')
    print(f'You won {score} points!')


# Calling the function:
names = ['Stor', 'Shepherd', 'Pax']
scores = [73, 82, 54]

for i in range(3):
    congrats_name_score(names[i], scores[i])

# Assigning a function to a variable:
congrats = congrats_name_score

# Calling the variable:
congrats('Peter', 99)

# Testing return:
n = print(names)
print(n)
# print returns nothing (None)


# Defining a function with a return value:
def num_square(num):
    return num**2


sqr = num_square(12)
print(f'12 x 12 = {sqr}')


# Defining a function with multiple return values:
def other_function():
    return 1, 2, 3, 4


num1, num2, num3, num4 = other_function()
print(other_function())
print(num1, num2, num3, num4)

# Using a random number:
from random import random
# random() generates a pseudo-random number between 0 and 1 (could be repeated)


def heads_tails():
    if random() > 0.5:
        return 'heads'
    return 'tails'


print(heads_tails())

# Parameters and Arguments:
# - Parameters are variables declared during the definition of the function
# - Arguments are the data passed during the calling of the function

# Order of the arguments must be the same of the parameters, except when using Keyword Arguments:
congrats_name_score(score=100, name='Kvothe')


# Functions with Default Parameters:
# Default Parameters must be declared last
def elevate(base, power=2):
    return base ** power


print(elevate(3))
print(elevate(3, 3))


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def math(a, b, op=add):
    return op(a, b)


print(math(3, 4))
print(math(3, 4, minus))

# Global, local and nonlocal variables:
# Local variables have priority over global ones
total = 0


def increment():
    global total
    # use global total
    total += 1
    return total


print(increment())
print(increment())


def outer():
    counter = 0
    # counter is local

    def inner():
        nonlocal counter
        # use local counter, but from exterior block
        counter += 1
        return counter
    return inner()


print(outer())
