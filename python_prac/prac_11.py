# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.
a = 1
b = 2

while b<10:
    if a == 1:
        print(f"{b}단")
    print(f"{b} x {a} = {a*b}")
    a +=1
    if a == 10:
        a = 1
        b +=1