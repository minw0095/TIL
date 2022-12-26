from collections import deque

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N) ]

q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
for a in range(N):
    for b in range(M):
        if graph[a][b] == 1:
            q.append([a,b])

def bfs():
    while q:
        x,y = q.popleft()

        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx,ny])

bfs()

for a in graph:
    for b in a:
        if b == 0:
            print(-1)
            exit()
    cnt = max(cnt, max(a))

print(cnt-1)

