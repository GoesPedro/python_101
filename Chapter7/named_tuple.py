# Collections Module - Named Tuple
# In Named Tuples, we specify the name of the tuple and some parameters
# It is like a constructor

from collections import namedtuple
# Creating a Named Tuple:
# form 1:
dog1 = namedtuple('dog', 'name race age')

# form 2:
dog2 = namedtuple('dog', 'name, race, age')

# form 3:
dog3 = namedtuple('dog', ['name', 'race', 'age'])

# Using a Named Tuple:
duna = dog1('Duna', 'Border Collie', 1)
pipoca = dog2(name='Pipoca', race='Brazilian Terrier', age=3)
zero = dog3('Zero', 'Undefined', 7)

# Accessing data:
print(duna.name, duna.age, duna.race)
print(pipoca.name, pipoca.age, pipoca.race)
print(zero.name, zero.age, zero.race)
