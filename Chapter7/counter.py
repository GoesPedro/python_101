# Collections - High-performance Container Datatypes
# Collections Module - Counter
# Counter receives a iterable value as argument and creates a
# dictionary-like object called "Collections Counter"

from collections import Counter
list1 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7]
result = Counter(list1)
print(result)
print(type(result))
# Each unique value in arguments turns into a key,
# and the value becomes the number of occurrences

text = """Lorem Ipsum is simply dummy text of the printing and
typesetting industry. Lorem Ipsum has been the industry's standard
dummy text ever since the 1500s, when an unknown printer took a
galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into
electronic typesetting, remaining essentially unchanged. It was
popularised in the 1960s with the release of Letraset sheets
containing Lorem Ipsum passages, and more recently with desktop
publishing software like Aldus PageMaker including versions of
Lorem Ipsum."""

words = text.split()
count = Counter(words)
print(count)
print(count.most_common(5))  # 5 most common words in the text