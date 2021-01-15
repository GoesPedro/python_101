# Like *args, is a parameter that accepts multiple inputs
# Different from *args, **kwargs needs named parameters, which will be transformed into a dictionary
# Both *args and **kwargs are optional parameters


def favorite_colors(**kwargs):
    print(type(kwargs))
    for person, color in kwargs.items():
        print(f"{person.title()}'s favorite color is {color}.")


favorite_colors(stor='green', shepherd='purple', pax='yellow')

# Parameters have to be declared IN THIS ORDER:
# 1. Required parameters
# 2. *args
# 3. Default parameters
# 4. **kwargs


def my_func(name, age, *args, marital_status=False, **kwargs):
    print(f'{name.title()} is {age} years old.')
    print(args)
    if marital_status:
        print('Married')
    else:
        print('Single')
    print(kwargs)


my_func('Stor', 53, 23, 54, 544)
my_func('Shepherd', 60, marital_status=False, java=False, python=True)
my_func('Pax', 301, 45, 523, 55, marital_status=True)

# Double asterisk can be used to identify a dictionary and unpack it:


def names(**kwargs):
    print(kwargs['first'], kwargs['last'])


who = {'first': 'Stor', 'last': 'Naïlo'}
names(**who)


def adding(a, b, c):
    return a + b + c


# Dictionary keys must be equal to parameters names
values = dict(a=1, b=2, c=3)
print(adding(**values))
