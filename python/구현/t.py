n = list(map(int, input().split()))


dic = {}
answer = []



for a in n:
    dic[a] = dic.get(a,0) +1

for a in dic:
    if dic[a] > 1:
        answer.append(dic[a])

if answer:
    print(answer)
else:
    print([-1])
