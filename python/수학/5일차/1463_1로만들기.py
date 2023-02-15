n = int(input())
dp =[0]*(n+1)


for a in range(2,n+1):
    cnt = dp[a-1]+1 # cnt는 현재 dp의 값을 저장, 2와 3으로 나누어 지지 않을 경우 이전 dp+1 한 것이 최소값
    if a % 2 == 0: # 만약 2로 나누어 지고
        if cnt > dp[a//2]+1: # 2로 나누어진 값의 dp 값이 위의 cnt 값보다 작을시(최소가 아니므로)
            cnt = dp[a//2]+1  # 현재 dp의 값은 2로 나누어진 값의 dp +1이 된다
    if a % 3 == 0:
        if cnt > dp[a//3]+1:
            cnt = dp[a//3]+1
        

    dp[a] = cnt

print(dp)



