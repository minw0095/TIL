import sys
input = sys.stdin.readline

n = input().strip()
m = input().strip()

dp = [[0]*(len(m)+1) for _ in range(len(n)+1)]
for a in range(1,len(n)+1):
    for b in range(1,len(m)+1):
        if n[a-1] == m[b-1]:
            dp[a][b] = dp[a-1][b-1] +1
        
        else:
            dp[a][b] = max(dp[a-1][b], dp[a][b-1])


print(dp[-1][-1])
        