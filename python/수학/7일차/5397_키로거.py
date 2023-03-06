

N = int(input())

for _ in range(N):
    t = list(input())
    res = []
    res2 = []
    cnt = 0
    for a in t:
        if a == '<':
            if res:
                res2.append(res.pop())
        
        elif a == '>':
            if res2:
                res.append(res2.pop())

        elif a == '-':
            if res:
                res.pop()
            

        else:
            res.append(a)
            
        
    
    print(''.join(res)+''.join(reversed(res2)))
