# Collections Module - Deque
# Deque is a high-performance list

from collections import deque

# Creating a deque:
deq = deque('geek')
print(deq)

# Adding elements to a deque:
deq.append('y')
print(deq)

deq.appendleft('Ultra')
print(deq)

# Removing items from a deque:
print(deq.pop())
print(deq)

print(deq.popleft())
print(deq)
