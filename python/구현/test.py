n = list(input().split())
t = 0
new = []

for a in len(n):
    if n[a] == "LONG":
        t += 16

    if n[a] == "INT":
        t += 8

    if n[a] == "FLOAT":
        if n[a+1] != "LONG" or  n[a+1] != "INT":
        t += 4

    if n[a] == "SHORT":
        t += 2
    
    if n[a] == "BOOL":
        t += 1

    if t >128:
        print("HALT")
        break