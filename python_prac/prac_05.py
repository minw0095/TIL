# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

number = [3,10,20]
count = 0
i = 0

for a in number:
    count += a
    i += 1
    print(count/i)