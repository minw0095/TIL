# from pprint import pprint

# n,m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]


# def makeWall(cnt):
#     if cnt == 3:
#         return

#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 pprint(graph)
#                 makeWall(cnt+1)
#                 graph[i][j] = 0

# makeWall(0)

def t(cnt):
    if cnt == 3:
        return
    
    for a in range(5):
        print(a,cnt)
        t(cnt+1)
        print('!',cnt)

t(0)