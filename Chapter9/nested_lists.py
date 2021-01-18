# Nested lists are lists within lists (matrices):
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lists)

# Accessing an element:
print(f'Element in position (1, 2) in a 3x3 matrix: {lists[0][1]}')

# Iterating (nested for):
for lis in lists:
    for n in lis:
        print(n)

# List comprehension (nested):
[[print(n) for n in lis] for lis in lists]

# Generating a 3x3 matrix:
print([[num for num in range(1, 4)] for line in range(3)])

# Generating a play in tic-tac-toe:
ttt = [['X' if not num % 2 else 'O' for num in range(1, 4)] for line in range(3)]

[print(line) for line in ttt]
