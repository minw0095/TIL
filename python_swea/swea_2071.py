import sys
sys.stdin = open("swea_2071.txt" , "r")


T = int(input())
for test_case in range(1, T + 1):
    number = map(int,input().split())
    print(f'#{test_case} {round(sum(number)/10)}')