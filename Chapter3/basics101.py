"""
dir() - list of attributes and methods
help() - documentation for a certain element
"""
print(dir('GeekUniversity'))

# Data input:
name = input("What's your name? ")
age = input('How old are you? ')

# Processing:

# Data output:
# Example Ver. 2.x:
#   print('Welcome, %s!' % name)
# Example Ver. 3.x:
#   print('Welcome, {0}! You are {1} years old'.format(name, age))
# From Ver. 3.7 (you can use "cast" inside the curly braces)
# Cast is the conversion between data types
print(f'Welcome, {name}! You were born in {2020 - int(age)}.')
