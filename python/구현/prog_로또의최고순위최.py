def solution(lottos, win_nums):
    answer = []
    rate = {
        6 : 1,
        5 : 2,
        4 : 3,
        3 : 4,
        2 : 5,
        1 : 6,
        0 : 6
    }
    max_rate = 0
    min_rate = 0
    
    for lotto in lottos:
        if lotto == 0:
            max_rate += 1
        
        elif lotto in win_nums:
            min_rate += 1
            max_rate += 1

    
        
    answer.append(rate[max_rate])
    answer.append(rate[min_rate])
    
    return answer