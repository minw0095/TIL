from collections import deque
from pprint import pprint


N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]



res = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
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

cnt = 0
for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:
            bfs(a,b)
            pprint(graph)
            cnt+=1

print(cnt)