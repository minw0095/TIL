n,m = map(int, input().split())

max = m
check = [True] * (max +1)

for a in range(2, int(max ** 0.5)):
    if check[a]:
        for b in range(a+a, max+1, a):
            check[b] = False

for a in range(2,m+1):
    if check[a]:
        print(a)
