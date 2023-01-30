t = ['a','b','b','c']
dic = {
}

for a in t:
    if not a in dic.keys():
        dic[a] = 1
    else:
        dic[a] += 1

for a in dic:
    print(a)
print(dic)

print(min(dic.values()))