a,b = map(int, input().split())



result = 0
for a in str(a*b)[::-1]:
    if a != '0':
        print(result)
        break
    else:
        result += 1