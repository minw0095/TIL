import sys
input = sys.stdin. readline

N = int(input())

res = []
for _ in range(N):
    t = input().split()
    if len(t) >1:
        res.append(int(t[1]))

    else:
        if t[0] =='pop':
            if len(res) != 0:
                print(res.pop())
            else:
                print(-1)
        if t[0] == 'size':
            print(len(res))
        if t[0] == 'empty':
            if len(res) >0 :
                print(0)
            else:
                print(1)
        if t[0] == 'top':
            if len(res) != 0:
                print(res[-1])
            else:
                print(-1)
