# Generators are Tuple Comprehensions
names = ['Carl', 'Cherita', 'Caspian', 'Christine', 'Karl']

lc = [name[0] == 'C' for name in names]  # List Comprehension
generator = (name[0] == 'C' for name in names)  # Generator Expression (generator object - iterable)

print(lc)
print(generator)
print(tuple(generator))

from sys import getsizeof

# List comprehension size:
list_comp = getsizeof([x * 10 for x in range(1000)])

# Set comprehension size:
set_comp = getsizeof({x * 10 for x in range(1000)})

# Dictionary comprehension size:
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Generator expression size:
gen = getsizeof(x * 10 for x in range(1000))

print('Memory required to do the same job:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')
