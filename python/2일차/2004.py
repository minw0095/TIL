# 2004 조합 0의 개수

a,b = map(int, input().split())

def cnt2(n):
    cnt = 0
    while n != 0:
        n = n //2
        cnt  += n

    return cnt


def cnt5(n):
    cnt = 0
    while n != 0:
        n = n //5
        cnt  += n

    return cnt

print(min(cnt2(a)-cnt2(b)-cnt2(a-b),cnt5(a)-cnt5(b)-cnt5(a-b)))