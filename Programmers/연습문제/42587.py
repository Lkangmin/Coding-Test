def solution(priorities, location):
    answer = 0
    idx = [i for i in range(len(priorities))]
    res = []
    
    while idx:
        cur = idx.pop(0)
        flag = 0
        
        for i in idx:
            if priorities[cur] < priorities[i]:
                idx.append(cur)
                flag = 1
                break
        
        if flag:
            continue
        
        res.append(cur)

    answer = res.index(location)
    return answer+1