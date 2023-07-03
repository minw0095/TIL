def solution(enroll, referral, seller, amount):
    answer = {}
    dic = {}
        
    for t in range(len(enroll)):
        dic[enroll[t]] =  referral[t] 
        answer[enroll[t]] = 0
        
    
    for t in range(len(seller)):
        x = seller[t]
        sell = amount[t] * 100
        answer[seller[t]] += sell - int(sell * 0.1)
        money = int(sell * 0.1)
        
        while dic[x] != "-":
            if money == 0:
                break
            answer[dic[x]] += money
            money = int(money*0.1)
            if dic[x] != "-":
                answer[dic[x]] -= money
            
            x = dic[x]
            
            
            
    
    return list(answer.values())