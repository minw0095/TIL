N = int(input())

cnt = 0
for a in range(1,N+1):
    if a <100:
        cnt +=1
    else:
        nums = list(str(a))
        if int(nums[1])-int(nums[0]) == int(nums[2])-int(nums[1]):
            cnt +=1
print(cnt)