# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

number = [0,20,100]
max = number[0]

for a in number:
    if a>max:
        max=a
print(max)