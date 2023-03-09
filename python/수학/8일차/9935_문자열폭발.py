n = input()
t = input()

stack = []
res = []

# for a in n:
#     if a in t:
#         stack.append(a)
#     else:
#         res.append(a)

#     while len(stack)>= len(t):
p=0
for a in n:
    res.append(a)

    if a == t[p]:
        stack.append(a)
        p += 1
    elif a !=t[p] and t[0]:
        stack.append(a)
        p = 1
    elif a !=t[p]:
        p = 0


    if p == len(t):
        for b in range(len(t)):
            res.pop()
            stack.pop()
        res = res+stack
        p = 0

print(res)
        

    

            
        
        

