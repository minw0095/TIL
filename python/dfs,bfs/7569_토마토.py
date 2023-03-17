from collections import deque
from pprint import pprint

N, M, H = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]
cnt = 0

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

q = deque()

def bfs():
    
    while q:
        z,y,x = q.popleft()

        for a in range(6):
            nx = x + dx[a]
            ny = y + dy[a]
            nz = z + dz[a]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                q.append([nz,ny,nx])

for a in range(H):
    for b in range(M):
        for c in range(N):
            if graph[a][b][c] == 1:
                q.append((a,b,c))
pprint(graph)
bfs()


for a in range(H):
    for b in range(M):
        cnt = max(cnt, max(graph[a][b]))    
        for c in range(N):
            if graph[a][b][c] == 0:
                print(-1)
                exit()
    

print(cnt-1)   

    

