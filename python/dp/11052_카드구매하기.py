n = int(input())
card = list(map(int, input().split()))
dp = []
price = 0

for a in range(1, n+1):
    price = max(price, a*(n//a) + )
