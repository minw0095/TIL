def solution(today, terms, privacies):
    
    dic = {}
    answer = []
    year, mon, day = today[0:4], today[5:7], today[8:]
    
    for term in terms:
        dic[term[0]] = term[2]
        
            
    for privacy in privacies:
        number = 1
        ex_year, ex_mon, ex_day, term_mon = int(privacy[0:4]), int(privacy[5:7]), int(privacy[8:10]), dic(privacy[-1])
        if ex_mon + int(term_mon) > 12:
            ex_year += 1
            ex_mon = ex_mon + int(term_mon) -12
        else:
            ex_mon += int(term_mon)
        
        if ex_day == 0:
            ex_mon -= 1
            ex_day = 28
        else:
            ex_day -= 1
        
        if ex_year == year:
            if ex_mon < mon:
                answer.append(number)
                
            elif ex_mon == mon:
                if ex_day < day:
                    answer.append(number)
            
            else:
                pass
        
        elif ex_mon < year:
            answer.append(number)
        
        else:
            pass
        
        number += 1
        
        
            
                                                        
    
    return answer
