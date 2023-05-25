n = int(input())

dp = [[0,1,1] for _ in range(n+1)]

for a in range(2,n+1):
    dp[a][0] = dp[a-1][0] + dp[a-1][1]
    dp[a][1] = dp[a-1][0]

    dp[a][2] = dp[a-1][0]*2 + dp[a-1][1]

print(dp[n][2])
