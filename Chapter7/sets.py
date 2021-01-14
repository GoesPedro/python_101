# Sets are from the mathematical Set Theory
# SETS DON'T HAVE:
# - duplicate values
# - ordinated values
# - indexes
# Sets are to store values when there is no need to ordination or duplicate values
# Sets are referred with curly braces {}, but without keys

# Defining a set (repeated values are excluded):
# Form 1:
s = set({2, 1, 5, 4, 3, 6, 7, 7, 2, 3})
print(s, type(s))

# Form 2:
r = {2, 1, 5, 4, 3, 6, 7, 7, 2, 3}
print(r, type(r))

# Example 1: using set to know the number of unique values in a list:
cities = ['São Paulo', 'London', 'Shanghai', 'New York', 'Tokyo', 'Shanghai', 'São Paulo', 'New York', 'London']
print(cities)
print(f'Number of visitors: {len(cities)}')
print(set(cities))
print(f'The visitors are from {len(set(cities))} different cities.')

# Adding elements to a set:
s = {99, 12, 42, 53, 23}
print(s)
s.add(int(input('Type a value to add it to the set: ')))
print(s)

# Removing elements from a set:
# Form 1 (by remove() method):
remove = int(input('Type a value to be removed from the set: '))
s.remove(remove)  # remove() returns an error if value not found
print(s)

# Form 2 (by discard() method):
discard = int(input('Type a value to be discarded from the set: '))
s.discard(discard)  # discard() does not return error if value not found
print(s)

# Copying a set can return a shallow copy (attribution) or a deep copy (copy() method)
# clear() method empties the set
# sum(), max(), min() and len() can be used as usual


# Mathematical methods for sets:
python_students = {'Peter', 'Stor', 'Shepherd', 'Ada'}
java_students = {'Peter', 'Ada', 'Nilo', 'Willian'}

print(f'Python students: {python_students}')
print(f'Java students: {java_students}')

# Union (union() method or pipe |):
all_1 = python_students.union(java_students)
print(f'union() method: {all_1}')

all_2 = python_students | java_students
print(f'pipe | notation: {all_2}')

# Intersection (intersection() method or ampersand &):
both_1 = python_students.intersection(java_students)
print(f'intersection() method: {both_1}')

both_2 = python_students & java_students
print(f'ampersand & notation: {both_2}')

# Difference (difference() method or minus -):
python_only_1 = python_students.difference(java_students)
java_only_1 = java_students.difference(python_students)
print(f'Python-only difference() method: {python_only_1}')
print(f'Java-only difference() method: {java_only_1}')

python_only_2 = python_students - java_students
java_only_2 = java_students - python_students
print(f'Python-only minus - notation: {python_only_2}')
print(f'Java-only minus - notation: {java_only_2}')
