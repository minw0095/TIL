n = int(input())
dp = [0]*(n+1)
color = [0] * (n+1)

for a in range(n):
    colors = list(map(int, input()))
    t = min(colors)