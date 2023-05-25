from collections import deque

n,k = map(int, input().split())


def top_sort():
    for _ in range(k):
        singer = list(map(int, input().split()))
        

