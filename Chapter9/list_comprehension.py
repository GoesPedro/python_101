# List Comprehension is used to generate a new list with processed data from another iterable
# List Comprehension Sintax:
# [ processed_data for raw_data in iterable ]

numbers = [1, 2, 3, 4, 5]

result = [num * 10 for num in numbers]

print(result)


def square(value):
    return value ** 2


result = [square(num) for num in numbers]

print(result)

# Same process using loop:
res = []
for n in numbers:
    res.append(n * 2)

print(res)

# Other applications:
print([bool(value) for value in [0, '', [], {}, True, -1, 'A', 1]])

print('evens from 1 to 9: ', [num for num in range(1, 10) if not num % 2])
print('odds from 1 to 9: ', [num for num in range(1, 10) if num % 2])

print([num * 2 if num % 2 else num / 2 for num in range(1, 10)])
