import sys
input = sys.stdin.readline

n = int(input())

dp = [1]*(n+1)

dp[1] = 3

x,y,z = 1,1,1


for a in range(2,n+1):
    y = x + z
    z = x + z
    x = dp[a-1]

    dp[a] = (x+y+z) %9901

print(dp[n])