n = input()

bar = 0 # 현재 쇠막대기의 갯수
res = 0 # 결과 값(총 쇠막대기의 갯수 + 레이저갯수* 레이저로 잘를때의 막대의갯수)
for a in range(len(n)-1):
    if n[a] == '(': #만약 왼 괄호가 있는데 
        if n[a+1] != ')': # 바로 오른 괄호가 나오지 않으면 쇠막대기의 개수이므로
            bar += 1 # 쇠막대기의 갯수에 더해주고
            res += 1 # 총쇠막대기의 갯수를 결과값에 더하기위해 +1
        else:
            res += bar # 만약 오른 괄호가 나오면 레이저이므로 현재 쇠막대기의 갯수를 결과 값에 더해줌
    
    else: # 오른 괄호면 
        if n[a-1] != '(': # 자신의 왼쪽에 왼괄호가 나오지 않으면 쇠막대기의 끝이므로
            bar -= 1 # 현재 막대기 갯수에서 1을 빼준다

print(res)