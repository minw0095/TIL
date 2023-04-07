import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))

res = 0
dp = -1001

for a in num:
    res += a
    dp = max(dp,res)

    if res < 0:
        res = 0



print(dp)