for t in range(int(input())):    
    n= int(input())

    cnt = 1
    for a in range(1, n+1):
        cnt *= a
    cnt_ = str(cnt)[::-1]


    for a in str(cnt_):
        if a != '0':
            print(a)
            break
