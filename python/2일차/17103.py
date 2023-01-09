# 17103 골드바흐 파티션

check = [True]*1000000


for a in range(2,1000+1):
    if check[a]:
        for b in range(a+a, 1000000, a):
            check[b] = False



for _ in range(int(input())):
    n =int(input())

    cnt =0

    for a in range(2,(n//2)+1):
        if check[a] and check[n-a]:
            cnt += 1

    print(cnt)
