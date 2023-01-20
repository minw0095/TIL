from queue import PriorityQueue

q = PriorityQueue()
t = PriorityQueue()
 

q.put(1)
q.put(2)
q.put(2)
t.put(2)
t.put(3)

print(q-t)