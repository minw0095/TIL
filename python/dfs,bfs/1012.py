from collections import deque

T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0

for t in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M  for _ in range(N) ]
    cnt = 0

    for _ in range(K):
        a,b = map(int, input().split())
        graph[b][a] = 1



    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1:
                bfs(a,b)
                cnt += 1
    
    print(cnt)


                    

        
