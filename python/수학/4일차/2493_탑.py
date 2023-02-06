import sys
input = sys.stdin.readline

N = int(input())

top = list(map(int, input().split()))
stack = []
res = [0] *N
for a in range(N):
    while stack:
        if stack[-1][1] > top[a]:
            res[a] = stack[-1][0] +1
            break
        else:
            stack.pop()

    stack.append([a,top[a]])



print(*res)
