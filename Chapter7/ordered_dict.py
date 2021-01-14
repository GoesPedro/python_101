# Collections Module - Ordered Dict
# In common dictionary, the order of the elements is not guaranteed.
# In an ordered dict, the order of the elements is guaranteed.

from collections import OrderedDict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True

ordered1 = OrderedDict({'a': 1, 'b': 2})
ordered2 = OrderedDict({'b': 2, 'a': 1})
print(ordered1 == ordered2)  # False
