# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 
# 2) for 문으로 각각 작성하시오.

# 1)while 문
n = int(input())
i = 1
total = 1

while i<n+1:
    total *=i
    i += 1
    print(total)


# 2)for 문
n = int(input())
i = 1

for a in range(1,n+1):

    i *= a
    print(i)