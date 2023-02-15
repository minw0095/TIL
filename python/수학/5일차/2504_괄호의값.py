N = input()

stack = []
num = 1 # 현재 값
res = 0 # 결과값

for a in range(len(N)):

    if N[a] == '(': # '(' 를 만나면 2를 곱해줌
        stack.append(N[a])
        num *= 2

    elif N[a] == '[':# '[' 를 만나면 3를 곱해줌
        stack.append(N[a])
        num *= 3
    
    elif N[a] == ')': # 만약 ')'를 만나면 
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