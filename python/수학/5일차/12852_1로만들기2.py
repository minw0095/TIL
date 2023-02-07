n = int(input())
dp =[0]*(n+1)


for a in range(2,n+1):
    cnt = dp[a-1]+1
    if a % 2 == 0:
        if cnt >= dp[a//2]+1:
            cnt = dp[a//2]+1
    if a % 3 == 0:
        if cnt >= dp[a//3]+1:
            cnt = dp[a//3]+1
    
    dp[a] = cnt

print(dp[n])



