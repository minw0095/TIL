from collections import deque

T = int(input())
def top_sort():
    res = 0
    q = deque()

    for a in range(1, n+1):
        if check[a] == 0:
            q.append((a, time[a]))
            

    while q:
        t,p = q.popleft()
        res += p
        if t == end:
            return res

        for a in graph[t]:
            check[a] -= 1

            if check[a] == 0:
                q.append((a, time[a]))

for _ in range(T):
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    check = [0] * (n+1)

    time = [0]
    time += list(map(int, input().split()))
    print(time)
    for _ in range(m):
        x,y = map(int, input().split())
        graph[x].append(y)
        check[y] += 1

    end = int(input())
    print(top_sort(),1)


            

