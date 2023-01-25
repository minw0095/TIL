import heapq

N = int(input())

res = []

for _ in range(N):
    t = int(input())
    heapq.heappush(res, t)
    p = len(res)
    if  p % 2 == 1 and p>1:
        print(f't {min(res[(p//2)+1],res[p//2])}')

    if p % 2 == 0:
        print(f't {min(res[(p//2)-1],res[p//2])}')


