# Dictionary Comprehension works similarly to List Comprehension
# Syntax:
# {key: value for key, value in iterable}

# Examples:
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
numb_list = [1, 2, 3, 4, 5, 4, 3, 2, 1]

squares = {key: value ** 2 for key, value in numbers.items()}
sqrs = {value: value ** 2 for value in numb_list}

print(squares)
print(sqrs)  # keys are not repeated

keys = 'abcde'
values = [1, 2, 3, 4, 5]

dic = {keys[i]: values[i] for i in range(0, len(keys))}

print(dic)

print({value: ('even' if not value % 2 else 'odd') for value in values})
