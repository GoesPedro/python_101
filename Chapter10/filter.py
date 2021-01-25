# Filter is for filtering the data of a collection, it returns an iterable filter object
import statistics

# Example 1 - data collected from a sensor:
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Mean:
mn = statistics.mean(data)
print(f'Mean: {mn}')

# Filter:
above = filter(lambda x: x > mn, data)
print(above, type(above))
print(list(above))

below = filter(lambda x: x < mn, data)
print(list(below))

# Example 2 - list with missing data:
countries = ['Argentina', '', 'Brazil', 'Chile', '', 'Ecuador', '', 'Bolivia', 'Peru', '']
print(countries)
print(list(filter(None, countries)))

# Example 3 - Filtering inactive users:
users = [
    {'username': 'samuel', 'tweets': ['i like cake', 'i love pizza']},
    {'username': 'johnny', 'tweets': []},
    {'username': 'sasha', 'tweets': ['i love stories']},
    {'username': 'christian', 'tweets': ['i like to travel', 'i love to love']},
    {'username': 'lilian', 'tweets': []}
]
print(users)

inactives = list(filter(lambda u: not u['tweets'], users))
print(inactives)

# Example 4 - Combining filter() and map():
names = ['Vanessa', 'Ana', 'Shirley', 'Carly', 'Mary']

instructors = list(map(lambda name: f'Your instrutor is {name}', filter(lambda name: len(name) < 6, names)))
for i in instructors:
    print(i)
