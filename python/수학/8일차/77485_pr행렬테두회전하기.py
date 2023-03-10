from pprint import pprint

def solution(rows, columns, queries):
    graph = [[] for _ in range(rows)]
    t = 1
    for a in range(rows):
        for b in range(columns):
            graph[a].append(t)
            t+=1

    pprint(graph)

solution(6,6,0)