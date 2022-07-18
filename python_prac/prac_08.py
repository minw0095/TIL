# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

number = [3,20,0,22,144,12]
max = number[0]
two_max =number[0]

for a in number:
    if a>max:
        two_max = max
        max=a
    elif two_max< a <max:
        two_max =a

print(two_max)