numbers = [4,1,2,1]
t = [[4,1,2,1]]
if 1 not in t:
    print('ss')

cnt = 0
res= []
for a in range(len(numbers)):
    if cnt+numbers[a]<= 4:
        cnt += numbers[a]
    else:
        cnt -= numbers[a]
        numbers[a] = -numbers[a]
res.append(numbers)

print(numbers,cnt)