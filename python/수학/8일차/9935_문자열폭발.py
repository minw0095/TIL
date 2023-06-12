n = input()
t = list(input())

res = []

p = 0
for a in range(len(n)):
    res.append(n[a]) # 현재 순회하는 단어들을 res에 넣어줌

    if n[a] == t[-1]: # 만약 폭발문자열의 마지막 문자열과 같다면
        if res[a-len(t)+1-p:a+1-p] == t: # 현재위치의 res에서 폭팔 문자열의 크기만큼 문자열이 폭발 문자열과 같다면
            for _ in range(len(t)):
                res.pop()  # 폭발 문자열을 빼주고
                p +=1 # p를 통해서 a의 크기를 보정해준다
        

if res:
    print(''.join(res))
else:
    print('FRULA')