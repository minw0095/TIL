from collections import deque

N = int(input())
counts = []
graph = []
for a in range(N):
    t = list(map(int, map(int, input())))
    graph.append(t)


def bfs(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0 
                q.append((nx,ny))
                cnt += 1
    
    counts.append(cnt)


for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:
            bfs(a,b)

counts.sort()
print(len(counts))
for a in counts:
    print(a)