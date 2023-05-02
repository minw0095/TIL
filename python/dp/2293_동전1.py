n,k = map(int, input().split())
coin = []
dp = [0 for _ in range(k+1)]
dp[0] = 1

for _ in range(n):
    coin.append(int(input()))

for a in coin:
    for b in range(1,k+1):
        if b - a >= 0:
            dp[b] += dp[b-a]

print(dp[k])