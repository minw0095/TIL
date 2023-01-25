import heapq

res = []
for _ in range(10):
    t = int(input())
    heapq.heappush(res, -t)


for _ in range(10):
    print(heapq.heappop(res))
    