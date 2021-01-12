# Type of data declared like:
# 'data'
# "data"
# '''data'''
# """data"""

name = 'Geek University'
print(f"name = {name}")
print(f"type(name) = {type(name)}")

multi_line = 'line 1 \nline 2'
print(multi_line)
print(f"multi_line.upper() = {multi_line.upper()}")

# Strings in python are like arrays with positions for each character
# String slicing:
print(f"name[0:4] = {name[0:4]}")
# After the colon, the index character is not included

print(f"name.split() = {name.split()}")
print(f"name.split('i') = {name.split('i')}")

# From first to last element, inverting:
print(f"name[::-1] = {name[::-1]}")

# Replace method:
print(f"name.replace('G', 'S') = {name.replace('G', 'S')}")
