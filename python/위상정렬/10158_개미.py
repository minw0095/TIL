w,h = map(int, input().split())
x,y = map(int, input().split())
t = int(input())
a,b = 1,1

for _ in range(t):
    if x == 0:
        a = -a
    if x == w:
        a = -a
    if y == 0:
        b = -b
    if y == h:
        b = -b

    x += a
    y += b

print(x,y)
    