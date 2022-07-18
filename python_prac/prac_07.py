# > 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# **min() 함수 사용 금지**

number = [100,20,0,22,144,12]
max = number[0]

for a in number:
    if a<max:
        max=a
print(max)