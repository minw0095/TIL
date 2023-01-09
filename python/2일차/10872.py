# 10872 팩토리얼

n = int(input())
cnt = 1
for a in range(1,n+1):
    cnt *= a
print(cnt)