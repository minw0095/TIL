from collections import deque


def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)

T = int(input())

for _ in range(T):
    num = deque(list(map(int, input().split())))
    p = num.popleft()
    result = 0
    for a in range(p):
        for b in range(a+1,p):
            result += gcd(num[a],num[b])
    
    print(result)

