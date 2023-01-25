import heapq
import sys
input = sys.stdin.readline

N = int(input())
res = []


for _ in range(N):
    
    t = int(input())
    if t ==0:
        if len(res) > 0:
            print(heapq.heappop(res)[1])
        else:
            print(0)
    
    else:
        heapq.heappush(res,(abs(t),t))
