n = int(input())

for _ in range(n):
    A = int(input())

    result = 0
    for a in range(1,A+1):
        cnt = A // a
        result += a*cnt

    print(result)