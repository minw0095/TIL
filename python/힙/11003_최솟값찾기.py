import heapq
import sys

input = sys.stdin.readline
N, L = map(int, input().split())

res = list(map(int, input().split()))

for a in range(1,N+1):
    if a-L+1 < 1:
        t = res[:a]
        heapq.heapify(t)
        print(heapq.heappop(t), end=' ')
    
    else:
        t = res[a-L:a]
        heapq.heapify(t)
        print(heapq.heappop(t), end= ' ')