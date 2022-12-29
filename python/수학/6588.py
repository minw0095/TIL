# n = int(input())

# if n >5:
#     nums = []
#     real = set()
#     for a in range(1,n+1):
#         rest = []
#         for t in range(1,a+1):
#             if a % t == 0 and a%2 == 1:
#                 rest.append(t)
#         if len(rest) == 2:
#             nums.append(a)
    
#     if len(nums) > 0:
#         for i in nums:
#             if n-i in nums:
#                 real.add(i)
    
#     if len(real) > 0:
#         print(f'{n} = {n-max(real)} + {max(real)}')
#     else:
#         print("Goldbach's conjecture is wrong.")
from sys import stdin



check = [True] * 1000000


for a in range(2,1001):
    if check[a] :
        for b in range(a+a, 1000000, a):
            check[b] = False



while True:
    N = int(stdin.readline())
    if N == 0:
        break
    for a in range(3,len(check)):
        if check[a] and check[N-a]:
            print(f'{N} = {a} + {N-a}')
            break

        






    


