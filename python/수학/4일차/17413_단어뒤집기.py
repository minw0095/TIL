a = input()


res = []
stack = []
i = 0

while i != len(a):
    if a[i] == '<':
        res.append(a[i])
        i += 1
        while a[i-1] != '>':
            res.append(a[i])
            i += 1
            

    elif a[i] == ' ':
        res.append(a[i])
        i += 1

    else:

        while True:
            stack.append(a[i])
            i += 1
            if i == len(a) or a[i] == '<' or a[i] ==' ':
                break

        res = res + stack[::-1]
        stack =[]


print(''.join(res))