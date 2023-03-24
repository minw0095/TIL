import heapq
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

indegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1



def d_sort():
    res = []
    q = []

    for a in range(1,n+1):
        if indegree[a] == 0:
            q.append(a)

    while q:
        t = heapq.heappop(q)
        res.append(t)

        for a in graph[t]:
            indegree[a] -= 1

            if indegree[a] == 0:
                heapq.heappush(q,a)
    
    for a in res:
        print(a, end=' ')

d_sort()




