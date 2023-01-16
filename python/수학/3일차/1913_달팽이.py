from pprint import pprint
N = int(input())
M = int(input())

graph = [[0]*N for _ in range(N)]

T = N

y = 0
i = 0
res = N**2
for _ in range((N//2)+1):
    for a in range(T):
        graph[y+a][y] = res -i
        i += 1
    for a in range(1,T):
        graph[y+T-1][y+a] =res -i
        i += 1
    for a in range(1,T):
        graph[y+T-1-a][y+T-1] =res -i
        i+=1
    for a in range(1,T-1):
        graph[y][y+T-1-a] =res-i
        i+=1
    y +=1
    T-=2


for a in graph:
    print(*a)

for a in range(N):
    for b in range(N):
        if graph[a][b] == M:
            print(a+1,b+1)
    
    
