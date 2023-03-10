n = input()
t = list(input())

stack = []
res = []

p = 0
for a in range(len(n)):
    res.append(n[a])

    if n[a] == t[-1]:
        if res[a-len(t)+1-p:a+1-p] == t:
            for _ in range(len(t)):
                res.pop()
                p +=1
        

if res:
    print(''.join(res))
else:
    print('FRULA')