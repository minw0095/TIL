N, M = map(int, input().split())

check = [False] * (N)
num = [a+1 for a in range(N)]

result = []

def dfs(cnt):

    if cnt == M:
        return print(*result)
    
    for a in range(N):
        if check[a]:
            continue

        check[a] = True
        result.append(num[a])
        dfs(cnt+1)
        result.pop()
        check[a] =False

dfs(0)