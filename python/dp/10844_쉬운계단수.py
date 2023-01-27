N = int(input())

# res = 0
# for a in range(1001,10000):
#     cnt = 0
#     for b in range(3):
#         if abs(int(str(a)[b]) -int(str(a)[b+1])):
#             cnt += 1
#     if cnt == 3:
#         res +=1
# print(res)

res = 0
for a in range(1000000,10000000):
    cnt = 0
    for b in range(6):
        if abs(int(str(a)[b]) -int(str(a)[b+1])) ==1:
            cnt += 1
    if cnt == 6:
        res +=1
print(res)
