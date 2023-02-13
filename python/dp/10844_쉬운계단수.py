# res = 0
# for a in range(1001,10000):
#     cnt = 0
#     for b in range(3):
#         if abs(int(str(a)[b]) -int(str(a)[b+1])):
#             cnt += 1
#     if cnt == 3:
#         res +=1
# print(res)
N = int(input())

dp = [[0 for _ in range(10)] for _ in range(101)]

for a in range(1,10):
    dp[1][a] = 1


for a in range(2,N+1):
    for b in range(10):
        if b == 0:
            dp[a][b] = dp[a-1][1]
        
        elif b == 9:
            dp[a][b] = dp[a-1][8]

        else:
            dp[a][b] = dp[a-1][b-1] + dp[a-1][b+1]


print(sum(dp[N])% 1000000000)