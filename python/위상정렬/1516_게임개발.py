from collections import deque

n = int(input())

check = [0] *(n+1)
time = [0]* (n+1)
dp = [0]* (n+1)
graph = [[] for _ in range(n+1)]

for a in range(1,n+1):
    build = list(map(int, input().split()))[:-1]
    time[a] = build[0]
    building = build[1:]

    for b in building:
        graph[b].append(a)
        check[a] += 1

def top_sort():
    res = [0] * (n+1)
    q = deque()
    
    for a in range(1,n+1):
        if check[a] == 0:
            q.append(a)
    
    while q:
        t = q.popleft()
        res[t] += time[t]
        for b in graph[t]:
            check[b] -= 1
            res[b] = max(res[b], res[t])
            if check[b] == 0:
                q.append(b)

    return res

result= top_sort()[1:]

for a in result:
    print(a)
    
        

