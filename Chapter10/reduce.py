# Since Python 3, reduce() is not a built-in anymore, it is part of the 'functools' library
# In most cases, a for loop is more legible
# Like map() and filter(), reduce() takes a function and an iterable as arguments
"""How reduce() works:
data = [a1, a2, a3, ..., an]
step 1. res1 = f(a1, a2)
step 2. res2 = f(res1, a3)
...
step n-1. res(n-1) = f(res(n-2), an)
reduce() returns the last result
"""
from functools import reduce
data = [2, 3, 5, 7]

mult = lambda x, y: x * y

res = reduce(mult, data)
print(res)

# Same result with normal loop:
res = 1
for i in data:
    res *= i

print(res)
