import sys
input = sys.stdin.readline
from collections import deque
import copy

N,M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs():
    q = deque()
    graph2 = copy.deepcopy(graph)
    for a in range(N):
        for b in range(M):
            if graph2[a][b] == 2:
                q.append((a,b))

    while q:
        x,y = q.popleft()
        
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            
            if 0 <= nx < N and 0 <= ny < M and graph2[nx][ny] == 0:
                graph2[nx][ny] = 2
                q.append([nx,ny])
    
    global answer
    cnt = 0

    for a in range(N):
        cnt += graph2[a].count(0)

    answer = max(answer, cnt)

def wall(t):
    if t == 3:
        bfs()
        return
        
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(t+1)
                graph[i][j] = 0


answer = 0
wall(0)
print(answer)


