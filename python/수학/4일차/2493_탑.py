import sys
input = sys.stdin.readline

N = int(input())

top = list(map(int, input().split()))

res = [0]

# for a in range(1,len(top)):
#     i = a -1
#     while i > 0:
#         if top[a] <= top[i]:
#             res.append(i+1)
#             break
#         i -= 1

#     if i == 0:
#         res.append(0)
    


print(*res)
