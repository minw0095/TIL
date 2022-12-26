from collections import deque
import sys
read = sys.stdin.readline


def bfs(x,y):
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,1,-1,1,0,-1]
    graph[x][y] = 0
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for a in range(8):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx,ny])
while True:                
    w,h = map(int, read().split())
    if w == 0 and h ==0:
        break
    graph = [list(map(int, read().split())) for _ in range(h)]

    cnt = 0


    for a in range(h):
        for b in range(w):
            if graph[a][b] == 1:
                bfs(a,b)
                cnt += 1
    print(cnt)

                    