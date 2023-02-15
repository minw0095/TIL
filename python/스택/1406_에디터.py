import sys
input = sys.stdin.readline

edit = list(input().rstrip())


N = int(input())
res = []
i = len(edit)
for _ in range(N):
    t = input().split()

    if t[0] == 'P':
        edit.append(t[1])

    if t[0] == 'L': 
        if edit:
            res.append(edit.pop())
    
    if t[0] == 'D':
        if res:
            edit.append(res.pop())
    
    if t[0] == 'B':
        if edit:
            edit.pop()
a =res[::-1]

print(''.join(edit+a))
