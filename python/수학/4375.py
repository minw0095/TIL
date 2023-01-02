# n = int(input())

# def plus(t):
#     if str(t) == '1'*len(str(t)):
#         return len(str(t))

#     t = t + n
#     plus(t)

# plus(n)
# 시간 복잡도 생각하자.str() 은 nlogn이다

while True:
    try:
        n = int(input())
    except:
        break
    t=-1
    num = 0
    while True:
        t += 1
        num += 10**t
        
        if num % n == 0:
            print(t+1)
            break


