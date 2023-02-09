import sys
input = sys.stdin.readline


n = int(input())
dp =[0]*(n+1)
check = [[] for _ in range(n+1)] 

check[1] = [1]

for a in range(2,n+1):
    cnt = dp[a-1]+1
    check[a] = check[a-1] + [a]
    if a % 2 == 0:
        if cnt > dp[a//2]+1:
            cnt = dp[a//2]+1
            check[a] = check[a//2] + [a]

    if a % 3 == 0:
        if cnt > dp[a//3]+1:
            cnt = dp[a//3]+1
            check[a] = check[a//3] + [a]

    dp[a] = cnt




print(dp[n])
print(*check[n][::-1])



