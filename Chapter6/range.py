# range(stop_value):
# stop value not included, standard starting value = 0, standard step = 1
for i in range(10):
    print(i)
print('---------------------')

# range(start_value, stop_value):
# standard step = 1
for i in range(1, 10):
    print(i)
print('---------------------')

# range(start_value, stop_value, step_length):
for i in range(1, 10, 2):
    print(i)
print('---------------------')

# reverse counting:
for i in range(10, 1, -2):
    print(i)
print('---------------------')

# Creating a list with range:
array = list(range(10))
print(array)
