list1 = [1, 5, 2, 7, 98, 23, 64, 64, 234, 12, 53]
list2 = list('Geek University')
list3 = []
list4 = list(range(10))

# Checking if a list contains a value:
value = 64

# Built-in method:
if list1.__contains__(value):
    print(f'list1 contains {value}')
else:
    print(f'list1 does not contain {value}')

# Using "in" (do not use "is"):
if value in list2:
    print(f'{value} is in list2')
else:
    print(f'{value} is not in list2')


# Ordering elements of a list:
# sort() is a destructive method
list1.sort()
list2.sort()
print(list1)
print(list2)

# reverse() is also destructive
list1.reverse()
print(list1)
# non-destructive reverse order:
list2 = list2[::-1]
print(list2)

# Counting the number of occurrences of a value in a list:
print(list1.count(value))
print(list2.count(value))


# Adding elements to a list:
# append() method -> whole argument added as an element
print(list3)
list3.append([77, 78, 79])
print(list3)

# extend() method -> values from iterable argument (e.g. string, list) added individually
list3.extend([77, 78, 79])
list3.extend('Peter')
print(list3)

# insert() method -> adds an item to the given position in the list
list4.insert(5, 'intruder')
print(list4)


# Removing elements from a list
# pop() -> destructive method, returns the removed value (last value as default)
removed = list3.pop()
print(list3)
print(removed)

removed = list3.pop(0)
print(list3)
print(removed)

# clear() -> destructive method, deletes all the elements
list3.clear()
print(list3)


# Length of the list:
length = len(list2)
print(length)


# Transforming string into list and vice-versa:
text = 'Peter Parker is Spider-man'
list5 = text.split()
print(list5)
text = ' '.join(list5)
print(text)


# Iteration in lists:
# for numbers:
total = 0
for e in list1:
    print(e)
    total += e
print(total)

# for strings:
total = ''
for e in list2:
    print(e)
    total += e
print(total)

# using while:
cart = []

while True:
    product = input("Type the product name or 'exit' to leave: ")
    if product != 'exit':
        cart.append(product)
    else:
        break

print(f"Your cart items: {cart}")


# List of variables:
e1 = 2
e2 = 7
e3 = 5
list6 = [e1, e2, e3]
print(list6)

e2 = 9
print(list6)
# altering the variable will NOT alter the list


# Accessing elements of a list:
list7 = ['arasaka', 'biotechnica', 'nicola', 'bushido', 'lizzies', 'arasaka', 'clouds', 'biotechnica']
print(list7[2])
print(list7[-1])  # last element

index = 0
while index < len(list7):
    print(list7[index])
    index += 1


# Getting the index of an element:
for index, name in enumerate(list7):
    print(index, name)

name = input('Type a name to check the index: ')
if list7.__contains__(name):
    print(list7.index(name))
    # index of the first occurrence
    print(list7.index(name, 2, 6))
    # start search from index 2 to index 5 (6 not included)
else:
    print('Name not found')


# Slicing revision:
# list[start:stop:step]
# range(start, stop, step)
list8 = list(range(10, 101, 10))
print(list8)
print(list8[1:8:2])  # from index 1 to 7 (8-1), step length = 2
print(list8[3:])     # from index 3 until the end
print(list8[:7])     # from the start to index 6
print(list8[3::2])   # from index 3 until the end, step length = 2
print(list8[::2])    # from the start until the end, step length = 2
print(list8[::-2])   # from the end until the start, step length = |-2|


# Inverting values in a list:
list9 = 'Peter Parker'.split()
print(list9)
list9[0], list9[1] = list9[1], list9[0]
print(list9)


# Sum, Maximum and Minimum (for list with only numbers):
list10 = [45, 52, -12, 53, -50, 23, -77, 98, 99, -21]
print(list10)
print(f"Sum of elements in list10 = {sum(list10)}")
print(f"Highest value in list10 = {max(list10)}")
print(f"Lowest value in list10 = {min(list10)}")


# Unpacking a list into variables:
# Number of variables must be equal to the list's length
list11 = [3, 5, 7]
num1, num2, num3 = list11
print(num1, num2, num3)


# Copying lists:
# by copy() method -> Deep Copy:
new_list = list11.copy()
new_list.append(9)
print(list11)
print(new_list)
# new_list is an independent list

# by attribution -> Shallow Copy:
dubious_new_list = list11
dubious_new_list.append(9)
print(list11)
print(dubious_new_list)
# dubious_new_list is just a pointer to list11
