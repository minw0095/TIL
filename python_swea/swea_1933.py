# import sys
# sys.stdin = open("swea_1933.txt" , "r")


# T = int(input())
# for test_case in range(1, T + 1):

N = int(input())

for a in range(1,N+1):
    if N%a == 0:
        print(a,end=' ')