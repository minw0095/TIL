import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
res = 0
while n != 0:
    n -= 1
    t = 2 ** n

    if r < t and c < t:
        res += 0
    
    elif r < t and c >= t:
        res += t * t
        c -= t
    
    elif r >= t and c < t:
        res += t * t * 2
        r -= t
    
    else:
        res += t * t * 3
        r -= t
        c -= t

print(res)