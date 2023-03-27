# 위상정렬이란 DAG(순회하지 않는 방향그래프)
# 따라서 진입차수가 0인 노드를 먼저 순회
# 이 문제는 작은 순서대로 순회를 해야하므로 큐대신 힙큐를 사용해서 순서를 정해준다.


import heapq
import sys
input = sys.stdin.readline

n,m = map(int, input().split()) #입력을 받아줄 n,m

indegree = [0] * (n+1) # 진입차수를 받아줄 그래프

graph = [[] for _ in range(n+1)] # 해당 노드들의 간선 정보를 입력받을 그래프

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y) #노드들의 간선 정보를 넣어주고
    indegree[y] += 1 # 진입차수의 갯수를 입력



def d_sort():
    res = [] # 답을 넣어줄 리스트
    q = [] # 진입차수가 0인 노드들을 넣어줄 리스트

    for a in range(1,n+1):
        if indegree[a] == 0: # 만약 진입차수가 0이면 q에 해당 노드를 넣어준다
            q.append(a)

    while q:
        t = heapq.heappop(q) # 앞에서 부터 빼주기 위해 heappop을 써주고 해당 q를 정리
        res.append(t) # 빠져나온 노드를 정답에 넣어주고

        for a in graph[t]: # 해당 노드의 간선들을 조회
            indegree[a] -= 1 # 해당 간선들의 진입차수를 1빼줌(진입하던 노드를 노드상에서 지웠으니)

            if indegree[a] == 0:
                heapq.heappush(q,a) # 힙큐를 사용해서 순서를 정해준다.
    
    for a in res:
        print(a, end=' ')

d_sort()




