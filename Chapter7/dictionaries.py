# Dictionaries are collections of the key-value type
# They are represented by curly braces {}
# Both key and value can be of any type of data (including lists, tuples and dictionaries)
# 2 forms of creating dictionaries:
# 1. Using curly braces:
countries = {'br': 'Brazil', 'usa': 'United States of America', 'uk': 'United Kingdom'}
print(countries, type(countries))

# 2. Using the dict() built-in function:
countries = dict(br='brazil', usa='united states of america', uk='united kingdom')
print(countries, type(countries))

# Dictionaries do not have indexes, gotta access via key or get() method:
# get() method returns 'None' type when key not found
# None type returns false in a Boolean expression
# get() can receive an output message as argument
print(countries['br'], countries['uk'])
print(countries.get('usa'), countries.get('ar'))
print(countries.get('ar', 'country not found'))

# Checking if a value is in the dictionary (these will return a boolean):
print('br' in countries)
print('ru' in countries)
print('united kingdom' in countries)

# Adding/Updating a pair in a dictionary:
# Form 1 (using attribution):
if (not countries.get('jp')):
    countries['jp'] = 'japan'
print(countries)

# Form 2 (using update() method):
china = {'cn': 'china'}
countries.update(china)
print(countries)

# Removing pairs from dictionaries:
# Form 1 (pop() method, which returns the removed value):
countries.pop('cn')
print(countries)

# Form 2 (del keyword):
del countries['jp']
print(countries)

# clear() method will erase all data from the dictionary:
# countries.clear()

# Copy via attribution returns a shallow copy
# Copy via copy() method returns a deep copy

# Unusual method to create dictionaries:
dictionary = {}.fromkeys(['a', 'b', 'c'], 'unknown')
print(dictionary)
