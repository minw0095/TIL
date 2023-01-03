
number = 1000000
num = [0]*(number+1)
total = [0]*(number+1)

for a in range(1,number+1):
    b = 1
    while a * b <= number:
        num[a*b] += a
        b += 1

for t in range(1,number+1):
    total[t] = total[t-1] + num[t]


n = int(input())
result = []
for _ in range(n):
    p = int(input())
    result.append(total[p])
print('\n'.join(map(str, result))+'\n')