n = int(input())
cnt = 0

def star(cnt):
    while cnt != 5:
        print('*',end='')
        cnt += 1
        star(cnt)

star(cnt)
