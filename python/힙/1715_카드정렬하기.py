import heapq

N = int(input())
num = []

for _ in range(N):
    t = int(input())
    heapq.heappush(num, t)

res = 0
for _ in range(N-1):
    a = heapq.heappop(num)
    b = heapq.heappop(num)
    res += a+b
    heapq.heappush(num, a+b)

print(res)