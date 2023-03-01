import sys
input = sys.stdin.readline
N = int(input())

num = {}
nums = []
new = int(input())
num[new] = 1
nums.append(new)
for _ in range(N-1):
    t = int(input())
    if t in num.keys():
        num[t] += 1
    else:
        num[t] = 1
    nums.append(t)

m = max(num.values())
res = []
number = sorted(num.keys())
nums = sorted(nums)

for a in number:
    if num[a] == m:
        res.append(a)



print(round(sum(nums)/N))
print(nums[(N//2)])
if len(res)>1:
    print(res[1])
else:
    print(res[0])
print(nums[N-1] - nums[0])

