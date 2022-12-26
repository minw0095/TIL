import sys
sys.stdin = open("input.txt", "r")

N = int(input())

def tower(N,a,b):
    if N == 1:
        print(a,b)
        return
   
    tower(N-1,a,6-a-b)
    print(a,b)
    tower(N-1,6-a-b,b)

print(2**N-1)
tower(N,1,3)
