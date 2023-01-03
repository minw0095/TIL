n = int(input())
number = 1000000
num = [0]*(number+1)
total = [0]*(number+1)

for a in range(1,number+1):
    b = 1
    while a * b <= number:
        num[a*b] += a
        b += 1

for a in range(1,1000001):
    total[a] = total[a-1] + num[a]



for _ in range(n):
    A = int(input())
    print(total[A])