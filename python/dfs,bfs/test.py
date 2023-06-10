from pprint import pprint
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[int(a) for a in input().strip()] for _ in range(n)]
visited = [[[-1,-1]]*m for _ in range(n)]

def dfs(x,y):
    q = deque()
    q.append((x,y,0,-1))

    while q:
        print(q)
        x,y,cnt,check = q.popleft()

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0 <= nx < n and 0<= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][0] == -1:
                    visited[nx][ny][0] = 2
                    q.append((nx,ny,cnt+1,check))

                if graph[nx][ny] == 1 and 0 <= nx+dx[a] < n and 0<= ny+dy[a] < m and graph[nx+dx[a]][ny+dy[a]] == 0 and  visited[nx][ny][0] == -1:
                    q.append((nx,ny,cnt+1,check+1))
                    visited[nx][ny][0] = 2
                    visited[nx][ny][1] = check+1

                if visited[nx][ny][1] == -1 and graph[nx][ny] == 0 and visited[nx][ny][0] == 2 and visited[nx][ny][1] == 0:
                    q.append((nx,ny,cnt+1,check-1))
                    visited[nx][ny][1] = check-1



                if nx == n-1 and ny == m-1:
                    return cnt+2

    return -1

print(dfs(0,0))
pprint(visited)