from pprint import pprint
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[int(a) for a in input().strip()] for _ in range(n)]
visited = [[[0,0]]*m for _ in range(n)]

def dfs(x,y,z):
    q = deque()
    q.append((x,y,0,-1))

    while q:
        print(q)
        x,y,z = q.popleft()

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0 and visited[x][y][z] == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                    


                if nx == n-1 and ny == m-1:
                    return cnt+2
                
    return -1

print(dfs(0,0))
pprint(visited)

