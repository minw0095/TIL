# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

word = input()
new_word =[]

for a in word:
    if a == 'a':
        print("")
    else:
        new_word.append(a)
    

print(''.join(new_word))