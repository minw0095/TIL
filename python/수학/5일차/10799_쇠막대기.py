n = input()

bar = 0
res = 0
for a in range(len(n)-1):
    if n[a] == '(':
        if n[a+1] != ')':
            bar += 1
            res += 1
        else:
            res += bar
    
    else: 
        if n[a-1] != '(':
            bar -= 1

print(res)