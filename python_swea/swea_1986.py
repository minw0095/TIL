import sys
sys.stdin = open("swea_1986.txt" , "r")


T = int(input())
for test_case in range(1, T + 1):

    count = 0
    N = int(input())
    for a in range(1,N+1):
        if a % 2 == 0:
            count -= a
        else:
            count += a
    print(f'#{test_case} {count}')


