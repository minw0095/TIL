import heapq

n,m = map(int, input().split())

res2 = [[i] for i in range(1,n+1)]
res = []
new = []

for a in range(m):
    t,s = map(int, input().split())
    heapq.heappush(res,[t,s])
    

for _ in range(len(res2)):
    print(heapq.heappop(res2))

