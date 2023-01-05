A = int(input())
t = list(map(int, input().split()))

for a in range(len(t)-1):
    B = []
    if t[a] < [a+1]:
        B.append(t[a])