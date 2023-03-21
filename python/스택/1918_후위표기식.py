n = input()

stack = []

res = ''

for a in n:
    if a.isalpha():
        res += a
    
    else:
        if a == '(':
          stack.append(a)

        elif a == '*' or a == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(a)

        elif a == '+' or a == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(a)
        
        elif a == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)


      
   