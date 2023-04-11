from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt = Counter(nums)
stack = []
res = [-1] * n



for a in range(n):
    while stack and cnt[nums[stack[-1]]] < cnt[nums[a]]:
        res[stack.pop()] = nums[a]
    print(res)
    stack.append(a)

print(*res)

    