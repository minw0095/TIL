n = int(input())
cnt = 0

def star(cnt):
    print('*')
    cnt += 1
    star(cnt)

