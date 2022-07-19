num = int(input())
total = []
while num != 0:
    total.append((num%10))
    num = num//10
for a in total:
    print(a,end= '')   
        