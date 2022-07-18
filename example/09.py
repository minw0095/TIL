# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#          fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)

#  fruit_count = {fruit: 1}를 선언하면 매 반복문 마다 초기화 시키므로 결국 반복문의 마지막 딕셔너리만 저장된다
#  따라서fruit_count[fruit] =  1를 통해서 모든 내용을 저장할수 있다.






from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] =  1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)
