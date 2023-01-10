N = input()

t = set(N)
dic = {}
cnt = 0

for a in t:
    dic[a] = N.count(a)
    if N.count(a) % 2:
        cnt +=1

sorted(dic.keys())

print(dic)