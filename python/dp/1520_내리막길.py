
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        
        if 0 <= nx <n and 0<= ny < m and graph[x][y] > graph[nx][ny]:
            cnt += dfs(nx,ny)

    dp[x][y] = cnt
    return dp[x][y]


print(dfs(0,0))

        