n = int(input())
dp = [0]*(n+1)
dp[1] = min(map(int, input().split()))
color = [0] * (n+1)
print(dp)

for a in range(n-1):
    r,g,b = map(int, input().split())
    t = min(r,g,b)
    color = [[1,r], [2,g], [3,b]]
