import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0]*(K+1) for _ in range(N+1)]
dp2 = [[0,0]]

for _ in range(N):
    dp2.append(list(map(int, input().split())))

for a in range(1,N+1):
    for b in range(1,K+1):
        w = dp2[a][0]
        v = dp2[a][1]
        
        if b < w:
            dp[a][b] = dp[a-1][b]
        else:
            dp[a][b] = max(dp[a-1][b], v+dp[a-1][b-w])

print(dp[N][K])



