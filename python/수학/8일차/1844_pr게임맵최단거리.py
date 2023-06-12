from collections import deque


def solution(maps):
    n,m = len(maps),len(maps[0])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque()
    q.append((0,0))

    while q:
        x,y = q.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
                q.append((nx,ny))
             
            if x == n-1 and y ==m-1:
                return maps[x][y]
    return -1 

