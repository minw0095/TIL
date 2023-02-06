graph = [list(map(int, input().split())) for _ in range(5)]

check = list(map(int, input().split()))
for _ in range(4):
    check += list(map(int, input().split()))
check_num = 0

cnt = 0
while cnt != 3:
    t = 0

    for a in check:
        for x in range(5):
            for y in range(5):
                if y == a:
                    graph[x][y] = 0
                if graph[x][y]
        