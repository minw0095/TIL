from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    cnt = 0
    q.append((numbers[0],cnt))
    q.append((-numbers[0],cnt))

    while q:
        a,b = q.popleft()
        b += 1
        if b < len(numbers):
            q.append((a+numbers[b],b))
            q.append((a-numbers[b],b))
        else:
            if a == target:
                answer += 1

    return answer


