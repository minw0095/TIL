num = int(input())
total = []
while num != 0:
    total.append((num%10))
    num = num//10
print(sum(total))    
        