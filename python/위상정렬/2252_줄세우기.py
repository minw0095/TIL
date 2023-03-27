from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

check = [0]* (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    t,p = map(int, input().split())
    graph[t].append(p)
    check[p] += 1

def top_sort():
    res = []
    q = deque()

    for a in range(1,n+1):
        if check[a] == 0:
            q.append(a)

    while q:
        x = q.popleft()
        res.append(x)

        for a in graph[x]:
            check[a] -= 1
            if check[a] == 0:
                q.append(a)
    
    print(*res)

top_sort()
