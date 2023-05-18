

w,h = map(int, input().split())
x,y = map(int, input().split())
t = int(input())

a = (t+x) // w
b = (t+y) // h

if a % 2 == 0 :
    n = (x+t) % w
else:
    n =  w - (x+t) % w

if b % 2 == 0:
    m = (y+t) % h
else:
    m = h - (y+t) % h

print(n,m)