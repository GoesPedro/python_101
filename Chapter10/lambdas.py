# Lambda functions are anonymous functions:
# Standard function declaration:
def func(x, y):
    return 3 * x + y


print(func(10, 1))

# Lambda function declaration (ugly form):
calc = lambda x, y: 3 * x + y

print(calc(10, 1))


# Another example:
name = 'Orson Scott Card'
print(name.split(' '))
print(name.split(' ')[-1])


authors = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'J. K. Rowling',
           'Douglas Adams', 'H. G. Wells']

print(authors)

# Sorting the list of authors by last name (nice form of lambda function):
authors.sort(key=lambda lastname: lastname.split(' ')[-1].lower())

print(authors)


# One more example:
def quadratic_function_constructor(a, b, c):
    """Returns a quadratic function: f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


result = quadratic_function_constructor(3, 4, -5)
print(result(0))
print(result(1))
print(result(2))
print(quadratic_function_constructor(1, 2, 3)(4))
