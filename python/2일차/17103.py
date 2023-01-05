n =int(input())

check = [True]*(n+1)

m = int(n ** 0.5)
for a in range(2,n+1):
    if check[a]:
        