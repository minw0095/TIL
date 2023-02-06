N = int(input())

num = [0] * 301
for a in range(1,N+1):
    num[a] = int(input())

check = [0] * 301
check[1] = num[1]
check[2] = num[1] + num[2]
check[3] = max(num[1]+num[3],num[2]+num[3])
# 마지막 계단의 전 계단(num[n-1])을 밟을 시 num[n-3]를 밟아야 하므로 check[n-3]을 더해줌
# 안 밟으면 (num[n-2])를 무조건 밟게 되므로 결국 check[a-2]를 더해줌
for a in range(4,N+1):
    check[a] = max(check[a-3]+num[a-1]+num[a], check[a-2]+num[a])

print(check[N])

