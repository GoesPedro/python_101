# all() only returns True if all elements from iterable are True or if the iterable is empty
# all() is like AND
print(all([0, 1, 2, 3]))  # False
print(all([1, 2, 3]))  # True
print(all(['Geek', 'False', 'True', True]))  # True

names = ['Carl', 'Cherita', 'Caspian', 'Christine', 'Karl']
print(all([name[0] == 'C' for name in names]))  # False

print(all([num for num in [2, 4, 6, 8, 10] if num % 2 == 1]))  # True
# inside all(), there is a list comprehension
# this will return an empty list, which all() converts into True


# any() only returns False if all elements from iterable is True
# any() is like OR
print(any([0, 1, 2, 3]))  # True
print(any([0, False, [], {}, ()]))  # False
print(any([-1, 0]))  # True
print(any([name[0] == 'C' for name in names]))  # True

# Just checking the iterables:
print([name[0] == 'C' for name in names])
print([num for num in [2, 4, 6, 8, 9, 10] if num % 2 == 1])
