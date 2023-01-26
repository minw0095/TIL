import heapq
import sys

input = sys.stdin.readline
N = int(input())

min_h = []
max_h = []

for _ in range(N):
    t = int(input())
    if len(min_h) == len(max_h):
        heapq.heappush(max_h, -1*t)
    else:
        heapq.heappush(min_h, t)
    
    if len(min_h) >= 1 and len(max_h) >= 1 and  max_h[0]*-1 > min_h[0]:
        a = heapq.heappop(min_h)
        b = -1 * heapq.heappop(max_h)

        heapq.heappush(max_h, -1*a)
        heapq.heappush(min_h, b)
    
    print(max_h[0] * -1)



