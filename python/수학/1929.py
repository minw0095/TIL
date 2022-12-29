M, N = map(int, input().split())

def prime(n):
    check = [True] * n

    m = int(n ** 0.5)
    for a in range(2,m+1):
        if check[a]:
            for b in range(a+a, n, a):
                check[b] = False
    
    return [i for i in range(2,n) if check[i]==True]

t = sorted(set(prime(N+1)) - set(prime(M)))

for a in list(t):
    print(a)
