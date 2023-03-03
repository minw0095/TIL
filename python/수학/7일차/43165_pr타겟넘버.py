import copy
res = []
def solution(numbers, target):

    t = 1
    while t != len(numbers):
        cnt = 0
        for a in range(len(numbers)):
            if cnt < target:
                if numbers[a] < 0:
                    cnt -= numbers[a]
                    numbers[a] = -numbers[a]
                else:
                    cnt += numbers[a]

            else:
                cnt -= numbers[a]
                numbers[a] = -numbers[a]

        numbers2 = copy.deepcopy(numbers)

        if cnt == target:
             if numbers2 not in res:
                res.append(numbers2)
        t += 1
        


solution([1,1,1,1,1],3)
print(len(res),res)

