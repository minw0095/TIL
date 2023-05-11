n, k = map(int, input().split())

dp = [[0]*201 for _ in range(201)]

for a in range(201):
    dp[1][a] = 1
    dp[2][a] = a+1


for a in range(2,201):
    dp[a][1] = a
    for b in range(2,201):
        dp[a][b] = (dp[a][b-1] + dp[a-1][b])% 1000000000

print(dp[k][n])