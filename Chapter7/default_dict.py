# Collections Module - Default Dict
# In normal dictionaries, when we try to access an nonexistent key,
# we get a KeyError.
# But in a Default Dict, we can inform a default value to nonexistent
# keys. A new key will be created and a value will be set to it
# when we try to access a nonexistent key.

from collections import defaultdict
dictionary = defaultdict(lambda: 'no info')
dictionary['course'] = 'Python Programming'
print(dictionary)
print(dictionary['other'])  # would return KeyError in common dictionary
print(dictionary)
