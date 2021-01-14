# Also known in Python as dictionaries {}

revenue = {'jan': 100, 'feb': 120, 'mar': 140}
print(revenue)

# Iterating in dictionaries:
for key in revenue:
    print(f'Month {key}: US$ {revenue[key]}')
    # print(f'{key}: {revenue.get(key)}')

# Lists of keys and values:
print(revenue.keys())
print(revenue.values())
for key, value in revenue.items():
    print(f'key = {key}, value = {value}')

# Max, Min and Sum:
print(max(revenue.values()))
print(min(revenue.values()))
print(sum(revenue.values()))
