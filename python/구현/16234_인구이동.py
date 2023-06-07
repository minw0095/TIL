from collections import deque

n, l, r = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]
check = []
t= 1

def bfs(i,j):
    global res
    cnt = 1
    visited[i][j] = 0
    total = graph[i][j]

    q = deque()
    q.append((i,j))

    while q:
        x,y = q.popleft()
        nx = [1,-1,0,0]
        ny = [0,0,1,-1]

        for a in range(4):
            dx = x +nx[a]
            dy = y +ny[a]

            check.append([x,y])
            if 0 <= dx < n and 0 <= dy < n:
                if l <= abs(graph[x][y] - graph[dx][dy]) <= r:
                    if visited[dx][dy] == -1:
                        q.append((dx, dy))
                        total += graph[dx][dy]
                        cnt += 1
                        visited[dx][dy] = 0
        
        res = total // cnt
    
    print(res,cnt,check)

while n:
    bfs(0,0)
    print(res)
    for a in check:
        [x,y] = a
        visited[x][y] = -1
        graph[x][y] = res

    break

print(graph)


