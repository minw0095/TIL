from collections import deque
from pprint import pprint
import copy


N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]



res = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 섬 구별용
def bfs(x,y):
    graph[x][y] = 2
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0<=nx<N and 0<=ny< N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 2
                    q.append((nx,ny))

                if graph[x][y] == 2 and graph[nx][ny] == 0:
                    t.append((x,y))

# 다리만들기 bfs
def bfs2():
    p = 0
    while t and p==0:
        x,y = t.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0<=nx<N and 0<=ny< N:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    t.append((nx,ny))

                if graph[nx][ny] == 1:
                    res.append(graph[x][y])
                    p +=1
                    

for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:
                t= deque()
                bfs(a,b)
                graph2 = [p[:] for p in graph]
                bfs2()
                pprint(graph)
                graph = [p[:] for p in graph2]

# for a in range(N):
#     for b in range(N):
#         if graph[a][b] == 1:
#                 t= deque()
#                 bfs(a,b)
#                 graph2 = copy.deepcopy(graph)
#                 bfs2()
#                 graph = copy.deepcopy(graph2)
#                 break
print(res)
print(min(res)-2)
