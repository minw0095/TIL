from collections import deque

n, l, r = map(int, input().split())

graph = [[list(map(int, input().split()))] for _ in range(n)]

def bfs():
    cnt = 1
    q = deque()

    while q:
        x,y = q.popleft()
        nx = [1,-1,0,0]
        ny = [0,0,1,-1]

        for a in range(4):
            dx = x +nx[a]
            dy = y +ny[a]

            if 0 <= nx < n and 0 <= ny < n:
                if l <= graph[x][y] + graph[dx][dy] <= r:
                    
