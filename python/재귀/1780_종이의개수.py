n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

res = []

def cut(x,y,n):
    color = graph[x][y]
    for a in range(x, x+n):
        for b in range(y, y+n):
            if color != graph[a][b]:
                cut(x, y, n//3)
                cut(x, y+n//3, n//3)
                cut(x+n//3, y, n//3)
                cut(x+n//3, y+n//3, n//3)
                return
    
    if color == -1:
        res.append(-1)
    
    elif color == 1:
        res.append(1)
    
    else:
        res.append(0)
cut(0,0,n)
print(res)
print(res.count(-1))
print(res.count(0))
print(res.count(1))