from collections import deque
from pprint import pprint
n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()
t = deque()

def water_bfs():
    global cnt
    while q:
        x,y,cnt = q.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if graph[x][y] == '*':
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    q.append((nx,ny,0))

            if graph[x][y] == 'S':
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = 'S'
                        q.append((nx,ny,cnt+1))
                
                
                    if graph[nx][ny] == 'D':
                        return 1


for a in range(n):
    for b in range(m):
        if graph[a][b] == '*':
            q.append((a,b,0))
        if graph[a][b] == 'S':
            t.append((a,b,0))

q = q +t

if water_bfs():
    print(cnt+1)
else:
    print('KAKTUS')
pprint(graph)




