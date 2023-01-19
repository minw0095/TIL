N, M = map(int, input().split())

check = [False] * N
num = [a+1 for a in range(N)]
res = []

def dfs(cnt):
    if cnt == M:
        return print(*res)
    
    for a in range(N):
        if check[a]:
            continue
        
        check[a] = True
        res.append(num[a])
        dfs(cnt+1)
        res.pop()
        check[a] = False

dfs(0)