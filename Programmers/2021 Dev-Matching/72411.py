from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in course:
        best_cnt = 0
        best_order = []
        comb = set()

        for j in orders:
            comb |= set(combinations(set(j), i))
        
        print(comb)
        for j in comb:
            temp = sorted(j)
            temp = ''.join(temp)
            cnt = 0 
            for k in orders:
                if set(temp) <= set(k):
                    cnt += 1
            if cnt > 1 and best_cnt < cnt:
                best_cnt = cnt
                best_order = []
                best_order.append(temp)
            elif cnt > 1 and best_cnt == cnt and temp not in best_order:
                best_order.append(temp)
        if best_cnt > 1:
            answer.extend(best_order)
    
    answer.sort()
    return answer