from collections import deque

T = int(input())
def top_sort():
    q = deque()

    for a in range(1, n+1):
        if check[a] == 0:
            q.append(a)
            dp[a] = time[a]

    while q:
        t = q.popleft()


        for a in graph[t]:
            check[a] -= 1
            dp[a] = max(dp[t] + time[a], dp[a])
            print(dp)

            if check[a] == 0:
                q.append(a)

for _ in range(T):
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    check = [0] * (n+1)
    dp = [0] * (n+1)

    time = [0] + list(map(int, input().split()))

    for _ in range(m):
        x,y = map(int, input().split())
        graph[x].append(y)
        check[y] += 1

    end = int(input())
    top_sort()

    print(dp[end])


            

