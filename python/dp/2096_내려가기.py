import sys
input = sys.stdin.readline

n = int(input())

max_dp = [0]*3
min_dp = [0]*3

max_tmp = [0]*3
min_tmp = [0]*3

for _ in range(n):
    x,y,z = map(int, input().split())
    for a in range(3):
        if a == 0:
            max_tmp[a] = x + max(max_dp[a], max_dp[a + 1])
            min_tmp[a] = x + min(min_dp[a], min_dp[a + 1])
        elif a == 1:
            max_tmp[a] = y + max(max_dp[a-1], max_dp[a], max_dp[a + 1])
            min_tmp[a] = y + min(min_dp[a-1], min_dp[a], min_dp[a + 1])
        else:
            max_tmp[a] = z + max(max_dp[a], max_dp[a - 1])
            min_tmp[a] = z + min(min_dp[a], min_dp[a - 1])
        
    for a in range(3):
        max_dp[a] = max_tmp[a]
        min_dp[a] = min_tmp[a]
    
print(max(max_dp), min(min_dp))
