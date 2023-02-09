# n = int(input())
# dp =[0]*(n+1)
# check = [[]] * (n+1)
# check[1] = [1]
# print(check)
# for a in range(2,n+1):
#     cnt = dp[a-1]+1
#     if a % 2 == 0:
#         if cnt > dp[a//2]+1:
#             cnt = dp[a//2]+1
#             check[a].append(check[a//2])
#     if a % 3 == 0:
#         if cnt > dp[a//3]+1:
#             cnt = dp[a//3]+1
#             check[a].append(check[a//2])

#     else:
#         check[a] = check[a-1]
    
#     dp[a] = cnt
#     check[a].append(a)

# print(check)
a = [[]]*3
a[0] = [0]
a[1] = []
a[2] = [2]
for t  in range(1,2):
    a[t+1] += a[t]
    a[t+1] += a[2]
    a[t].append(t)

print(a)


