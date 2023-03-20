n = input()

stack = []
stack2 =[]
res = []

for a in n:
    res.append(a)
    if res[-1] == '(' or res[-1] == ')':
        res.pop()
    elif res[-1] == '/' or res[-1] == '*' or res[-1] == '+' or res[-1] == '-':
        stack.append(res.pop())
    
    
    if stack:
        if stack[-1] == '/' or stack[-1] == '*':
            res.append(stack.pop())
        elif a == n[-1]:
            while stack:
                res.append(stack.pop())

print(res,stack)