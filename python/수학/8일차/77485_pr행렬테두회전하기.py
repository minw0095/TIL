from pprint import pprint
from collections import deque

def solution(rows, columns, queries):
    res = []
    
    graph = [[] for _ in range(rows)]
    t = 1
    for a in range(rows): # 먼저 주어진 크기의 그래프를 만들어주기
        for _ in range(columns):
            graph[a].append(t)
            t+=1
    
    dx = [0,1,0,-1]  #오른방향, 아래방향, 왼방향, 윗방향으로 조회할 좌표
    dy = [1,0,-1,0]

    for a in queries:
        i = 0 # 방향의 순서를 정할 변수
        q = deque() # 지나갈 때마다 수를 넣어줄 덱큐
        x,y = a[0]-1,a[1]-1 # 제일 먼저 시작할 부분 [2,2,5,4] 경우 [2,2]에서 시작하는 좌표 
        cnt = t # 제일 작은지 비교해줄 변수
        q.append((graph[x][y],graph[x][y])) # 반복문을 시작하기 위해서 [2,2]에 해당하는 수를 넣어줌, 뒤숫자는 작은수를 비교하기 위함

        while q: #q가 있을 때
            # 만약  순회하는 구간의 꼭지점 좌표에 도달할 시 방향을 i의 크기를 변화 시켜 방향을 바꿔준다
            if [x,y] == [a[0]-1,a[3]-1] or [x,y] == [a[2]-1,a[3]-1] or [x,y] == [a[2]-1,a[1]-1]:
                i = (i+1) % 4 
                

            x = x + dx[i] # 해당방향으로 계속 진행
            y = y + dy[i]
            

            p,z = q.popleft() # 이전 좌표 그래프의 값, 최소 값을 위한 값을 꺼내준다 
            cnt = min(cnt,z) # 최소 값을 계속해서 갱신
            q.append((graph[x][y],graph[x][y])) # 현재 그래프의 값을 q에 넣고
            graph[x][y] = p # 현재 그래프의 값은 이전 좌표 그래프의 값이 된다
            
            if x == a[0]-1 and y == a[1]-1:
                res.append(cnt)
                break
    
    return res
        
            


    
    
print(
solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
