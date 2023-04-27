n = int(input())
card = [0]+list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
price = 0

for a in range(1, n+1):
    for b in range(1, a+1):
        dp[a] = max(dp[a], dp[a-b] + card[b])

print(dp[n])
