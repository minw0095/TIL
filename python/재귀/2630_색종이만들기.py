n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

white = []
blue = []

def cut(x,y,n):
    color = graph[x][y]
    for a in range(x,x+n):
        for b in range(y,y+n):
            if color != graph[a][b]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    
    if color == 0:
        white.append(0)
    else:
        blue.append(1)

cut(0,0,n)
print(len(white))
print(len(blue))
