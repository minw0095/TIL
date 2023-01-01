import sys
from collections import deque
input = sys.stdin.readline

N, M =map(int, input().split())
graph = [list(input()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,cnt):
    max_ = 0
    q = deque()
    q.append((x,y,cnt))
    check[x][y] = 1

    while q:
        x,y,cnt = q.popleft()
        if max_ < cnt:
            max_ = cnt
        
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == "L" and check[nx][ny] == 0:
                q.append((nx,ny,cnt+1))
                check[nx][ny] = 1
                
    return max_

result = 0
check_li =[]
for a in range(N):
    for b in range(M):
        if graph[a][b] == "L":
            check = [[0]*M for _ in range(N)]
            result = max(result,bfs(a,b,0))
    
print(result)


                
                



