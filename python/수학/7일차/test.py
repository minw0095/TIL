a = [1,2,3]
b = [5,6,7]

from collections import deque

c = deque(a) + deque(b)

print(c)