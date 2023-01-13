n,m = map(int, input().split())

if m > 10000000:
    m = 10000000
max = m
check = [True] * (max +1)

for a in range(2, int(max ** 0.5)+1):
    if check[a]:
        for b in range(a+a, max+1, a):
            check[b] = False

for a in range(n,m+1):
    if check[a]:
        if a == int(str(a)[::-1]):
            print(a)

print(-1)