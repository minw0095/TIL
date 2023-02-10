import sys
input = sys.stdin.readline

n = int(input())
j = [0] * 10001
for t in range(1,n+1):
    j[t] = int(input())

dp = [0] * (10000+1)
dp[1] = j[1]
dp[2] = j[1] + j[2]
dp[3] = max(dp[2],j[1]+j[3], j[2]+j[3])

for a in range(4,n+1):
    dp[a] = max(dp[a-1], dp[a-3]+j[a]+j[a-1], dp[a-2]+j[a])


print(dp[n])
 