import sys
sys.stdin = open("input.txt", "r")
from collections import deque

N,M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]


    while q:
        x,y = q.popleft()
        
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append([nx,ny])

for a in range(N):
    for b in range(M):
        if graph[a][b] == 2:
            bfs(a,b)

for a in range(N):
    for b in range(M):
        if graph[a][b] == 0 



print(graph)
        

