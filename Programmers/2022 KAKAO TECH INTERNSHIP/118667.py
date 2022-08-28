from collections import deque

def solution(queue1, queue2):
    nq1 = deque(queue1)
    nq2 = deque(queue2)
    s1 = sum(nq1)
    s2 = sum(nq2)
    cnt = 0
    
    # len*2 +2 인 이유
    # 한쪽에 값이 쏠려있는 형태가 대표적. 예시) [1,1,1,8,10,9] [1,1,1,1,1,1] (14회 확인필요)
    for i in range(len(queue1)*2 + 2):
        if s1 == s2:
            break
        
        if s1 > s2:
            temp = nq1.popleft()
            nq2.append(temp)
            s1 -= temp
            s2 += temp
            cnt += 1
        else:
            temp = nq2.popleft()
            nq1.append(temp)
            s1 += temp
            s2 -= temp
            cnt += 1
    
    if sum(nq1) != sum(nq2):
        cnt = -1
    
    return cnt
