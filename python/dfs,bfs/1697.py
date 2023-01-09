# 1697 숨바꼭질
from collections import deque

N, K = map(int, input().split())


def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()

        if x == K:
            print(graph[x])
            break
        for a in [x-1, x+1, x*2]:
            if 0 <= a <= 100000 and graph[a] == 0 :
                graph[a] += graph[x] +1
                q.append(a)

graph = [0] * 100001   

bfs()