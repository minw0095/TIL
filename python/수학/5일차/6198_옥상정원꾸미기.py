import sys
input = sys.stdin.readline

N = int(input()) # 주어진 빌딩수

stack = [] #
cnt = 0

roof = [int(input()) for _ in range(N)] # 빌딩들의 리스트

for a in range(N):
    
    while stack: # 스택리스트에 숫자가 들어 있을 경우
        if stack[-1] > roof[a]: # 최근 스택이 현재 빌딩보다 높을 경우
            break #스택에 들어 있는 빌딩들 모두 현재 빌딩의 지붕을 볼 수 있으므로 빠져나온다
        else:
            stack.pop() # 작은 경우 못보므로 스택에서 없애고 그전 빌딩들도 조사한다.

    if stack:
        cnt += len(stack) # 현재빌딩의 지붕을 볼 수 있는 빌딩들의 집합들을 계속 더해줌
    
    stack.append(roof[a]) # 현재 빌딩을 스택에 넣어준다.
    


print(cnt)