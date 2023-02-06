import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split())) #  주어진 수를 리스트로 
stack = [] # 
res = [-1] * N # 모든 NGE를 먼저 -1로 정의

for a in range(N):
    while stack: #스택 존재시
        if num[a] > stack[-1][1]: #현재의 수가 스택
            res[stack[-1][0]] = num[a]
            stack.pop()
        else:
            break

    stack.append([a,num[a]]) # NGE리스트의 인덱스와 비교할 수를 넣어줌


print(*res)