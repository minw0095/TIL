N, K = map(int, input().split())

dp = []*101
dp2 = []*101

dp[1] = dp2[1][1]
if dp2[2][0] + dp2[1][0] <=7:
    dp[2] = dp2[2][1] + dp2[1][0]
else:
    dp[2] = max(dp2[2][1], dp2[1][0])


for a in range(N):
    dp2[a].append(list(map(int, input().split())))

