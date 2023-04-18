n, r, c = map(int, input().split())

graph = [[0]*(2**n) for _ in range(2**n)]
cnt = 0
print(graph)
def Z(x, y, t):
    global cnt
    cnt += 1
    graph[x][y] = cnt
    cnt += 1
    graph[x][y+1] = cnt
    cnt += 1
    graph[x+1][y] = cnt
    cnt += 1
    graph[x+1][y+1] = cnt
    t *= 2

    if t != 

Z(0,0,0)
print(graph)