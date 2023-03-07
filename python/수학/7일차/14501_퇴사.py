N = int(input())

T = []
P = []

dp = [0 for _ in range(N+1)]

for a in range(1,N+1):
    t,p = map(int, input().split())
    T.append(t)
    P.append(p)

for a in range(N-1, -1,- 1):
    if T[a] + a > N:
        dp[a] = dp[a+1]
    
    else:
        dp[a] = max(dp[a+1], dp[T[a] + a] + P[a])

print(dp[0])

