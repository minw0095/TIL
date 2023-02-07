N = input()

satck = []
for a in range(len(N)):
    if N[a] == '(':
        if N[a+1] != ')':
            