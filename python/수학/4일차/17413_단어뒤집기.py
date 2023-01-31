a = input().split()
a.reverse()
res = []
print(a)
for t in a:
    res.append(t[::-1])

print(*res)