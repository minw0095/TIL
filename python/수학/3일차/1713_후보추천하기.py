N = int(input()) #사진틀
M = int(input()) #추천 수
num = list(map(int, input().split())) # 추천 리스트

t = {} # 딕셔너리로 추천후보와 추천수를 받을 것을 생각

for a in num:
    if len(t.keys()) < N: #처음은 사진틀 만큼만 딕셔너리를 채움
        if not a in t.keys():
            t[a] = 1
        else:
            t[a] += 1

    else:               # 사진틀의 수를 벗어났을 때
        if a in t.keys(): # 만약 추천자가 사진틀에 있을시 카운트를 늘림
            t[a] += 1
        else:             # 없을 시
            for b in t.keys(): #키값안에
                if t[b] == min(t.values()): # 추천수가 가장 적은 수와 같으면
                    del t[b]   # 그 후보자를 삭제(가장 오래된것)
                    t[a] = 1  # 그리고 다음 후보자를 넣어줌
                    break  # 추천수가 같은 후보자를 또 지우면 안되므로 for문을 탈출하고 맨처음 for문으로 다시돌아감

print(*sorted(t.keys()))

