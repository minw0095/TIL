n = int(input())
dp = [0]*(n+1)
num = [0]*(n+1)
for a in range(len(list(map(int, input().split())))):

color = [0] * (n+1)
print(dp)

for a in range(n-1):
    r,g,b = map(int, input().split())
    t = min(r,g,b)
    color = [[1,r], [2,g], [3,b]]

    for a in num
