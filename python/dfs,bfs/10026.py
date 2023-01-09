from collections import deque

N = int(input())

graph = [list(input()) for _ in range(N) ]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def real_red(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    while q:
        x,y = q.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0<= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 'R':
                    graph[nx][ny] = 0
                    q.append([nx,ny])

def green(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    while q:
        x,y = q.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0<= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 'G':
                    graph[nx][ny] = 0
                    q.append([nx,ny])
def red(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    while q:
        x,y = q.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0<= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    graph[nx][ny] += 2
                    q.append([nx,ny])

def blue(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 1

    while q:
        x,y = q.popleft()
        
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0<= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 'B':
                    graph[nx][ny] = 1
                    q.append([nx,ny])
cnt0 = 0
cnt1 = 0
cnt2 = 0

for a in range(N):
    for b in range(N):
        if graph[a][b] == 'R':
            real_red(a,b)
            cnt0 += 1
        if graph[a][b] == 'G':
            green(a,b)
            cnt0 += 1
        if graph[a][b] == 'B':
            blue(a,b)
            cnt2 += 1

for a in range(N):
    for b in range(N):
        if graph[a][b] == 0:
            red(a,b)
            cnt1 += 1

print(cnt0+cnt2,cnt1+cnt2)
            

        
