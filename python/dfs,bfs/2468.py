from collections import deque
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
max_num = 0

for a in range(N):
    for b in range(N):
        if graph[a][b] > max_num:
            max_num = graph[a][b]


dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs():
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > num and check[nx][ny] == False:
                check[nx][ny] = True
                q.append([nx,ny])

result = 0
for t in range(max_num):
    check = [[False]*N for _ in range(N)]
    num = t
    cnt = 0
    for a in range(N):
        for b in range(N):
            if graph[a][b] > num and check[a][b] == False:
                dfs(a,b)
                cnt +=1
    if cnt > result:
        result = cnt
print(result)

