import heapq
N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]

num.sort()

result = []

heapq.heappush(result, num[0][1])

for a in range(1,N):
    if num[a][0] >= result[0]:
        heapq.heappop(result)
    
    heapq.heappush(result, num[a][1])

print(len(result))

