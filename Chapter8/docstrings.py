# Docstrings are comments limited by triple double quotes
"""This is a Docstring"""
# Docstrings are used to create documentation for functions
# They can be accessed with the built-in function help(func_name)
# Or using the .__doc__ property (func_name.__doc__)


def say_hi(n):
    """
    A function that returns the string 'Hi ' multiplied by n.
    :param n: Number of times the string 'Hi ' will be printed.
    :return: Returns the string 'Hi ' multiplied by n.
    """
    return 'Hi ' * n


print(say_hi(30))
help(say_hi)
print(say_hi.__doc__)
