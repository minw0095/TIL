N = int(input())

result = [1] * (N+1)

check = [1] * 1001
check[2] = 1
check[3] = 2
for a in range(4,1001):
    check[a] = check[a-2] + check[a-1]

for a in range(2,N+1):
    result[a] = check[a-1] +result[a-1]

print(result[N]%10007)