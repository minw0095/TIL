# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)
# count도 total을 따라서 반복해야 하지만 count의 위치가 for문에서 벗어나 있기 때문에 한번만 실행된 1의 값을 가진다
# 따라서 count 앞에 Tab을 눌러서 for문에 넣어주고 total//count는 나머지를 없애기 때문에 /로 바꿔줘야한다.




number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)