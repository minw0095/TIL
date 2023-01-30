from pprint import pprint
# N = int(input())
# M = int(input())

# graph = [[0]*N for _ in range(N)]

# T = N

# y = 0
# i = 0
# res = N**2
# for _ in range((N//2)+1):
#     for a in range(T):
#         graph[y+a][y] = res -i
#         i += 1
#     for a in range(1,T):
#         graph[y+T-1][y+a] =res -i
#         i += 1
#     for a in range(1,T):
#         graph[y+T-1-a][y+T-1] =res -i
#         i+=1
#     for a in range(1,T-1):
#         graph[y][y+T-1-a] =res-i
#         i+=1
#     y +=1
#     T-=2


# for a in graph:
#     print(*a)

# for a in range(N):
#     for b in range(N):
#         if graph[a][b] == M:
#             print(a+1,b+1)

#2번째 풀이
N = int(input())
M = int(input())

graph = [[0]*N for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n= N**2
x,y = 0,0
i = 0


while True:

    graph[x][y] = n

    x = x + dx[i]
    y = y + dy[i]

    if n == 1:
        break

    if not 0<=x<N or not 0<=y<N or graph[x][y] != 0:
        x = x - dx[i]
        y = y - dy[i]
        i = (i+1) % 4
    else:
        n -= 1
    
for a in graph:
    print(*a)


for a in range(N):
    for b in range(N):
        if graph[a][b] == M:
            print(a+1,b+1)
    
