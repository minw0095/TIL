N = input()

stack = []
num = 1
res = 0

for a in range(len(N)):

    if N[a] == '(':
        stack.append(N[a])
        num *= 2

    elif N[a] == '[':
        stack.append(N[a])
        num *= 3
    
    elif N[a] == ')':
        if not stack :
            res =0
            break

        
        if N[a-1] == '(':
            res += num
            num //= 2
            stack.pop()

        if N[a-1] != '(' and stack:
            if stack[-1] == '(':
                
                num //= 2
                stack.pop()

    elif N[a] == ']':
        if not stack  :
            res = 0
            break

        if N[a-1] == '[':
            res += num
            num //= 3
            stack.pop()
        
        if N[a-1] != '[' and stack:
            if stack[-1] == '[':
                
                num //= 3
                stack.pop()

if stack:
    print(0)

if not stack:
    print(res)