N = input()

p = set(N)
dic = {}
cnt = 0

for a in p:
    dic[a] = N.count(a)
    if N.count(a) % 2:
        cnt +=1

t = sorted(dic.keys())
n_len = len(N)
alp = ''
last = ''


if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    for a in t:
        if not dic[a] % 2:
            alp += a*(dic[a]//2)
        if  dic[a] % 2:
            alp += a*(dic[a]//2)
            last = a

alp = alp +last +alp[::-1]


print(alp)