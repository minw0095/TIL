# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)
# if char == "a" or "e" or "i" or "o" or "u"를 봤을 때 char에 모음이 있을 경우 참이므로 반복문 실행시 모두 참이되어서 'HappyHacking' 전체의 문자열의 길이가 나오게 된다
# 따라서 모음이 따로 들어가 있는 리스트를 만들어 if문을 만들어야 한다.



word = "HappyHacking"

count = 0
alph = ['a','e','i','o','u']

for char in word:
    if char in alph:
        count += 1

print(count)