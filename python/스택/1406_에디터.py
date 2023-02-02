import sys
input = sys.stdin.readline

edit = list(input())

N = int(input())

i = len(edit)
for _ in range(N):
    t = input().split()
    if len(t) > 1:
        edit.insert(i, t[1])
        i += 1
    else:
        if t[0] == 'L':
            if i>0:
                i -= 1
        
        if t[0] == 'D':
            if i < N-1:
                i += 1
        
        if t[0] == 'B':
            if i > 0:
                del edit[i-1]
                i -= 1

print(''.join(edit))
