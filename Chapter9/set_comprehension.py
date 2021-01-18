# Works like List Comprehension, but using curly braces
# Syntax:
# {processed_value for raw_value in iterable}

# Examples:
squares = {i ** 2 for i in range(1, 8)}
print(squares)

characters = {char for char in 'geek university python course'}
print(characters)
