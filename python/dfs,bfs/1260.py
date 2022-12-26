from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]


for t in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for a in graph:
    a.sort()

visit1 = [False] * (N+1)
visit2 = [False] * (N+1)

def dfs(start):
    visit1[start] = True
    print(start, end=' ')
    for a in graph[start]:
        if not visit1[a]:
            dfs(a)

def bfs(start):
    stack = deque([start])
    visit2[start] = True
    
    
    while stack:
        cur  = stack.popleft()
        print(cur, end=' ')

        for ad in graph[cur]:
            if not visit2[ad]:
                visit2[ad] = True
                stack.append(ad)

dfs(V)
print()
bfs(V)
