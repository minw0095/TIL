import sys
input = sys.stdin.readline

n,k = map(int, input().split())

tem = list(map(int, input().split()))
res = []
cnt = sum(tem[0:k])
res.append(cnt)

for a in range(1,n-k+1):
    cnt += tem[a+k-1] - tem[a-1]
    res.append(cnt)

print(max(res))
