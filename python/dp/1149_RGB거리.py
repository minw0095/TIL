import sys
input = sys.stdin.readline

n = int(input())
dp = []

for a in range(n):
    dp.append(list(map(int, input().split())))

for a in range(1,n):
    dp[a][0] = min(dp[a-1][1], dp[a-1][2]) +  dp[a][0]
    dp[a][1] = min(dp[a-1][0], dp[a-1][2]) +  dp[a][1]
    dp[a][2] = min(dp[a-1][0], dp[a-1][1]) +  dp[a][2]

print(min(dp[n-1]))