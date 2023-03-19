n = int(input())

dp = [0]* (31)
dp[2] = 3
if n>3:
    for a in range(4,n+1):
        if a % 2 == 0:
            dp[a] = dp[a-2]*3 + sum(dp[:a-2]) * 2+ 2


print(dp[n])