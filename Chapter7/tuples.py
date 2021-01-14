# Tuples are very much like lists, but with 2 basic differences:
# 1. Tuples are can't have their elements altered;
# 2. Tuples are represented by parenthesis ();
# They can be created using parenthesis or not, but always with comma
# Tuples must be used whenever we need a collection that won't have its elements altered
# They are iterable, their values are countable and can be any type of data

tpl1 = (1, 2, 3)
tpl2 = 1, 2, 3
print(type(tpl1), type(tpl2))  # both are tuples

tpl3 = (4)      # not a tuple
tpl4 = (4,)     # tuple
tpl5 = 4,       # tuple
print(type(tpl3), type(tpl4), type(tpl5))

# Creating a tuple with range:
tpl6 = tuple(range(11))
print(tpl6, type(tpl6))

# Tuple unpacking:
tpl7 = ('Geek University', 'Python Programming')
school, course = tpl7
print(school, course, type(school), type(course))

# Adding values to or removing values from tuples is not possible
# Sum, Max, Min and Len work like in lists
# Tuples are immutable, but their values can be overwritten:
tpl8 = 1, 2, 3
tpl9 = 4, 5, 6

tpl8 += tpl9
print(tpl8)

# Counting elements:
tpl10 = tuple('Geek University')
print(tpl10.count('e'))

# Slicing is as in lists:
tpl11 = tuple(range(6))
print(tpl11[2:5])
print(tpl11[::-1])

# Why use tuples instead of lists:
# - Tuples are faster than lists;
# - Tuples make the code safer (immutable).

# Copy of a tuple is always a deep copy
