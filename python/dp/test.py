from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
cnt = Counter(nums)
print(cnt[1])