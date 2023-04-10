n,k = map(int, input().split())
t = input()
stack = []

for a in t:
    while stack and stack[-1] < a and k >0:
        stack.pop()
        k -= 1

    stack.append(a)

if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))



