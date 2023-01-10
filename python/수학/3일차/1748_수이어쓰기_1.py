N = int(input())

t= len(str(N))

result = 0
cnt = 0
i = 1
while cnt < t:
    cnt += 1
    if cnt == t:
        result += (N+1 - (10**(i-1))) * i
    else:
        result += (9*(10**(i-1))) * i
    
    i +=1

print(result)