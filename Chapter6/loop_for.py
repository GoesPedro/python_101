name = 'Geek University'
indexes = [0, 2, 4, 6, 8, 10, 12, 14]

# Printing every character in a string:
for i in name:
    print(i)

# Printing the corresponding characters in a string from a list of indexes:
for i in indexes:
    print(name[i])

# Using indexes from a range:
# range(start_value, last_value, step size)
# Last value in range is not included
for i in range(1, 10, 2):
    print(i)

# enumerate(str) returns a tuple (index, 'character')
for i in enumerate(name):
    print(i)
# underscore (_) in python is something to be discarded
# _ and char are the two values in the tuple
for _, char in enumerate(name):
    print(char, end='.')

print('')

emoji = '\U0001F602'
for j in range(3):
    for i in range(1, 11):
        print(emoji * i * (j+1))
