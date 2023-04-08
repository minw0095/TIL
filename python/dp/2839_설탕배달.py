n = int(input())

dp = [-1]*(n+1)

for a in range(3,n+1):
    if a==3:
        dp[a] =1

    if a==5:
        dp[a] =1

    if dp[a-3] > 0:
        dp[a] = dp[a-3] +1

    if dp[a-5] > 0:
        dp[a] = dp[a-5] +1

    if dp[a-3] > 0 and dp[a-5] > 0:
        dp[a] = min(dp[a-3]+1, dp[a-5]+1)


print(dp[n])
    