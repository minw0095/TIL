import heapq
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

indegree = [0] * (n+1)

graph = [[] for _ in range(m+1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    indegree[x] += 1


def d_sort():
    res = []
    q = deque()

    for a in range(1,n+1):
        if indegree[a] == 0:
            q.append(a)




