import sys
input = sys.stdin.readline
N = int(input())

dp = [[1]*10 for _ in range(N+1)]
res = [0] * (N+1)
res[1] = 10

for a in range(2,N+1):
    for b in range(10):
        if b ==0 :
            dp[a][b] = res[a-1]
        else:
            dp[a][b] = dp[a][b-1] - dp[a-1][b-1]



    res[a] = sum(dp[a])

print(res[N]%10007)